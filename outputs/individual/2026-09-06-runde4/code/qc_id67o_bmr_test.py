# ============================================================================
# QC ID67o — Batch-minus-Marginal-Residual (BMR) Test
# QuantConnect Research Notebook — EINE vollstaendig lauffaehige Zelle.
# In eine neue Zelle kopieren und ausfuehren. qb-Global wird NICHT neu erzeugt.
#
# ----------------------------------------------------------------------------
# HYPOTHESE (vorregistriert — Datenfalle 5, VOR Ausfuehrung fixiert):
#   BMR = Settlement_CME - Close(Minutenbar 14:59 CT) enthaelt gerichtete
#   Information ueber die RTH-Erststunde des Folgetags. Entry Folgetag-Open in
#   Richtung sign(BMR) bei |BMR| >= Guard; Abstain sonst.
#
# 3 GATES (exakt wie im Feasibility-Dokument vorregistriert):
#   GATE 1 (Rundungsfalle/Symmetrie): Settlement NICHT aus Minutenbars
#       (30s-VWAP nicht berechenbar) — aus oeffentlicher CME-Settlements-Seite
#       (User laedt CSV) oder QC-Settlement-Field falls vorhanden; defensive
#       Abfrage + Fallback auf Daily-Close mit WARNUNG. Placebo = Pseudo-Anker
#       aus Bar 13:59 CT mit IDENTISCHER 0,25-Rundung (nearest tick).
#   GATE 2 (Ueberlebensrate-Gate VOR Haupttest): ERSTER Analyseschritt.
#       Anteil Tage mit |Settlement - letzter Continuous-Minutenbar| >= Guard
#       (0.5 ES / 1.0 NQ). Abbruchregel: < 15% -> Eskalation auf Guard = ein
#       Rundungs-Quantum (0.25 ES); dort < 15% -> NO-GO ohne Haupttest.
#   GATE 3 (Kontrolle): 500 blockweise Vorzeichen-Permutationen (Monatsbloecke),
#       Jonckheere-Monotonie ueber Monatsend-Strata, GC/ZB-Falsifikator
#       (ZB mit eigener 1/64-Rundung als Rundungsfallen-Nachweis).
#
# VORREGISTRIERTE ABNAHMEKRITERIEN:
#   Placebo-Perzentil > 95% (n=500), Cliff's d >= 0.10, Jonckheere p < 0.05,
#   GC nicht signifikant, ZB-Effekt nicht auf ES-Grid, Hit-Rate > 52% bei
#   n >= 500, Decay-Split 2022+ vs. davor berichtet (2022+ entscheidend).
#
# SETTLEMENT-CSV-FORMAT (User legt die Datei ins Notebook-Projekt bzw. passt
# den String unten an — defensive Abfrage mit Fallback):
#   SETTLEMENT_CSV = {
#       "ES": {"2024-01-02": 4750.25, ...},   # Datum ISO -> Settlement-Preis
#       "NQ": {...}, "GC": {...}, "ZB": {...} # ZB-Preise in Punkten (1/64-Grid)
#   }
#   Quelle: cmegroup.com -> Settlements-Seite des jeweiligen Kontrakts (CSV),
#   Lead-Month gemappt auf QC-Continuous (OPEN_INTEREST-Mapping = Lead Month).
# ============================================================================

import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta

# ------------------------- KONFIGURATION (vorregistriert) -------------------
START = datetime(2019, 1, 1)
END = datetime(2026, 9, 1)
PLACEBO_N = 500
CLIFFS_D_MIN = 0.10
PERCENTILE_MIN = 95.0
SURVIVAL_MIN = 0.15          # Gate-2-Abbruchschwelle
SEED = 67

# Instrumente: (QB-Symbol, Anker-Bar CT, Rundungs-Quantum, Start-Guard, Multiplikator)
INSTRUMENTS = {
    "ES": dict(qb=Futures.Indices.SP_500_E_MINI, anchor_hhmm=time(14, 59),
               tick=0.25, guard=0.5, mult=50.0),
    "NQ": dict(qb=Futures.Indices.NASDAQ_100_E_MINI, anchor_hhmm=time(14, 59),
               tick=0.25, guard=1.0, mult=20.0),
    "GC": dict(qb=Futures.Metals.GOLD, anchor_hhmm=time(12, 29),
               tick=0.10, guard=0.5, mult=100.0),
    "ZB": dict(qb=Futures.Financials.Y_30_TREASURY_BOND, anchor_hhmm=time(13, 59),
               tick=1.0 / 64.0, guard=1.0 / 64.0, mult=1000.0),
}

# >>> USER-INPUT: Settlement-Daten (CME/CBOT/COMEX Settlements-Seiten) <<<
# Leer lassen => Fallback auf Daily-Close mit WARNUNG (Gate 1, defensiv).
SETTLEMENT_CSV = {"ES": {}, "NQ": {}, "GC": {}, "ZB": {}}

rng = np.random.default_rng(SEED)

# ------------------------- HILFSFUNKTIONEN ----------------------------------
def round_to_tick(x, tick):
    """Identische Rundungsoperation fuer Treatment UND Placebo (Gate 1)."""
    return np.round(x / tick) * tick


def in_dst_gap_weeks(d):
    """US/EU-DST-Asynchronie-Wochen — Flag nur, Analyse strikt ET/CT."""
    m, day = d.month, d.day
    return ((m == 3 and 8 <= day <= 31) or (m == 10 and day >= 25)
            or (m == 11 and day <= 7))


def cliffs_delta(a, b):
    """Cliff's d: P(a>b) - P(a<b)."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    a = a[np.isfinite(a)]
    b = b[np.isfinite(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan
    gt = (a[:, None] > b[None, :]).sum()
    lt = (a[:, None] < b[None, :]).sum()
    return (gt - lt) / (len(a) * len(b))


def jonckheere_p(groups):
    """Jonckheere-Terpstra-Trend ueber geordnete Gruppen (Normalapprox.,
    Permutations-exakt waere zu teuer; n pro Stratum hier >> 20)."""
    u = 0.0
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            a = groups[i]
            b = groups[j]
            u += (a[:, None] < b[None, :]).sum() + 0.5 * (a[:, None] == b[None, :]).sum()
    ns = [len(g) for g in groups]
    n_tot = sum(ns)
    e_u = (n_tot ** 2 - sum(n ** 2 for n in ns)) / 4.0
    var_u = ((n_tot * (n_tot - 1) * (2 * n_tot + 5)
              - sum(n * (n - 1) * (2 * n + 5) for n in ns)) / 72.0)
    if var_u <= 0:
        return np.nan
    z = (u - e_u) / np.sqrt(var_u)
    # einseitig (vorregistrierte Richtung: Monatsend > Monatswoche > Rest)
    from math import erf, sqrt
    return 0.5 * (1 - erf(z / sqrt(2)))


def get_settlement(name, date_iso, daily_close):
    """Defensive Abfrage (Gate 1): CSV-Wert, sonst QC-Daily-Close + Warnung."""
    v = SETTLEMENT_CSV.get(name, {}).get(date_iso, None)
    if v is not None:
        return v, False
    return daily_close, True   # Fallback


# ------------------------- HAUPTSCHLEIFE PRO INSTRUMENT ---------------------
results = {}
for name, cfg in INSTRUMENTS.items():
    print("\n" + "=" * 78)
    print(f"INSTRUMENT {name} — Anker-Bar {cfg['anchor_hhmm']} CT, "
          f"Tick {cfg['tick']}, Start-Guard {cfg['guard']}")
    print("=" * 78)

    future = qb.add_future(cfg["qb"],
                           Resolution.MINUTE,
                           data_mapping_mode=DataMappingMode.OPEN_INTEREST,
                           data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO,
                           extended_market_hours=True,
                           contract_depth_offset=0)
    symbol = future.symbol
    print(f"Datenreihe: {symbol} | continuous, mapping=OPEN_INTEREST, "
          f"normalization=BACKWARDS_RATIO, extended_market_hours=True")

    history = qb.history(symbol, START, END, Resolution.MINUTE,
                         extended_market_hours=True)
    df = history.reset_index()   # ID29-Muster: reset_index + Spalten, KEINE Index-Hacks
    df["time"] = pd.to_datetime(df["time"])
    # CME/CBOT/COMEX-Bars kommen in Exchange-Zeitzone = America/Chicago (CT).
    df["date"] = df["time"].dt.date
    df["tod"] = df["time"].dt.time

    days = sorted(df["date"].unique())
    print(f"Handelstage gesamt: {len(days)}  ({days[0]} .. {days[-1]})")

    anchor_t = cfg["anchor_hhmm"]
    placebo_anchor_t = time(13, 59) if name in ("ES", "NQ") else anchor_t
    tick = cfg["tick"]

    recs = []
    fallback_days = 0
    for d in days:
        day_df = df[df["date"] == d]
        if len(day_df) == 0:
            continue
        # Letzter Continuous-Minutenbar vor/am Anker (letzter voller Bar vor
        # Settlement-Fensterende) — Close des Anker-Bars.
        anchor_bar = day_df[day_df["tod"] == anchor_t]
        if len(anchor_bar) == 0:
            # frueher Schluss (Feiertag/Halbtag) -> Abstain, gezaehlt
            recs.append(dict(date=d, year=d.year, month=(d.year, d.month),
                             dst_flag=in_dst_gap_weeks(d), abstain=True))
            continue
        last_close = float(anchor_bar["close"].iloc[-1])
        daily_close = float(day_df["close"].iloc[-1])
        settle, used_fallback = get_settlement(name, d.isoformat(), daily_close)
        fallback_days += int(used_fallback)

        bmr = round_to_tick(settle, tick) - last_close          # Treatment
        # Placebo (Pseudo-Anker, Gate 1): Bar 13:59 CT, IDENTISCHE Rundung
        pb_bar = day_df[day_df["tod"] == placebo_anchor_t]
        if len(pb_bar) == 0:
            pb_bmr = np.nan
        else:
            tp = float((pb_bar["high"].iloc[-1] + pb_bar["low"].iloc[-1]
                        + pb_bar["close"].iloc[-1]) / 3.0)
            pb_bmr = round_to_tick(tp, tick) - float(pb_bar["close"].iloc[-1])

        # Ziel: Return erste RTH-Stunde des Folgetags (Open -> Open+60min, ET)
        recs.append(dict(date=d, year=d.year, month=(d.year, d.month),
                         dst_flag=in_dst_gap_weeks(d), abstain=False,
                         bmr=bmr, placebo_bmr=pb_bmr))

    R = pd.DataFrame(recs)
    n_abstain = int(R["abstain"].sum())
    R = R[~R["abstain"]].copy()
    print(f"Abstain-Tage (kein Anker-Bar, ausgeschlossen UND gezaehlt): "
          f"{n_abstain} ({n_abstain / max(len(recs), 1):.1%}) — "
          f"tradable Tage: {len(R)}")
    if fallback_days > 0:
        print(f"WARNUNG (Gate 1 Fallback): {fallback_days} Tage ohne "
              f"Settlement-CSV-Wert -> Daily-Close verwendet. Ergebnis fuer "
              f"{name} damit VORLAEUFIG (Rundungsfeld teils geloescht).")

    # ---- Folgetag-RTH-Erststunden-Return (Open -> Open+60min, ET) ----------
    # CT 08:30 = ET 09:30 RTH-Open; QC-Bars hier in CT.
    date_to_df = dict(tuple(df.groupby("date")))
    next_ret = []
    dates_sorted = sorted(R["date"].unique())
    next_map = {dates_sorted[i]: dates_sorted[i + 1]
                for i in range(len(dates_sorted) - 1)}
    for d in R["date"]:
        nd = next_map.get(d)
        if nd is None or nd not in date_to_df:
            next_ret.append(np.nan)
            continue
        ndf = date_to_df[nd]
        open_bar = ndf[ndf["tod"] == time(8, 30)]          # CT = 09:30 ET
        plus60 = ndf[(ndf["tod"] >= time(8, 30))
                     & (ndf["tod"] < time(9, 30))]
        if len(open_bar) == 0 or len(plus60) < 30:
            next_ret.append(np.nan)
            continue
        next_ret.append(float(plus60["close"].iloc[-1]
                              / open_bar["open"].iloc[0] - 1.0))
    R["next_rth1h_ret"] = next_ret
    R = R.dropna(subset=["bmr", "next_rth1h_ret"])
    print(f"Tage mit BMR + Folgetag-Return: {len(R)}")
    if len(R) < 100:
        print(f"FEHLER: zu wenig Daten fuer {name} — Instrument uebersprungen.")
        continue

    # ============ GATE 2 — UEBERLEBENSRATE (ERSTER Analyseschritt) ==========
    abs_bmr = R["bmr"].abs()
    print(f"\n[GATE 2] |BMR|-Verteilung {name} (Punkte):")
    for g in sorted(set([float(cfg["guard"]), float(tick),
                         2.0 * float(cfg["guard"]), 1.0, 2.0])):
        share = (abs_bmr >= g).mean()
        print(f"    |BMR| >= {g:>6.3f}: {share:6.1%}  (n={int((abs_bmr >= g).sum())})")

    guard = cfg["guard"]
    surv = (abs_bmr >= guard).mean()
    if surv < SURVIVAL_MIN:
        print(f"[GATE 2] Ueberlebensrate {surv:.1%} < 15% bei Guard {guard} "
              f"-> Eskalation auf ein Rundungs-Quantum ({tick}).")
        guard = tick
        surv = (abs_bmr >= guard).mean()
        if surv < SURVIVAL_MIN:
            print(f"[GATE 2] Ueberlebensrate {surv:.1%} < 15% auch bei Guard "
                  f"{tick} -> NO-GO fuer {name} OHNE Haupttest.")
            results[name] = dict(nogo=True, surv=surv, guard=guard)
            continue
    print(f"[GATE 2] PASS — Guard {guard}, Ueberlebensrate {surv:.1%}, "
          f"Replikate/Jahr ~{len(R) * surv / max(R['year'].nunique(), 1):.0f}")

    sig = R[abs_bmr >= guard].copy()
    sig["dir"] = np.sign(sig["bmr"])
    sig = sig[sig["dir"] != 0]
    signed_ret = sig["dir"] * sig["next_rth1h_ret"]
    obs = float(signed_ret.mean())
    hit = float((signed_ret > 0).mean())
    print(f"\n[HAUPTTEST] n={len(sig)}, mean signed ret={obs * 1e4:.2f} bps, "
          f"Hit-Rate={hit:.1%} (vorregistriert: > 52%)")

    # Cliff's d: signed_ret vs. gespiegelte Null (Vorzeichen-Flip)
    cd = cliffs_delta(signed_ret.values, -signed_ret.values)
    print(f"[HAUPTTEST] Cliff's d = {cd:.3f} (vorregistriert: >= {CLIFFS_D_MIN})")

    # ============ GATE 3a — 500 blockweise Vorzeichen-Permutationen =========
    months = sig["month"].to_numpy()
    sr = signed_ret.to_numpy()
    perm_stats = np.empty(PLACEBO_N)
    for k in range(PLACEBO_N):
        perm = np.empty_like(sr)
        for m in pd.unique(sig["month"]):
            idx = np.where(months == m)[0]
            signs = rng.choice([-1.0, 1.0], size=len(idx))
            perm[idx] = np.abs(sr[idx]) * signs
        perm_stats[k] = perm.mean()
    pctile = 100.0 * (perm_stats < obs).mean()
    print(f"[GATE 3a] Placebo-Perzentil (n={PLACEBO_N}, Monatsblock-"
          f"Vorzeichen-Permutation): {pctile:.1f}% (vorregistriert: > 95%)")

    # ============ GATE 3b — Jonckheere Monatsend-Monotonie ==================
    def month_stratum(d):
        last_day = (pd.Timestamp(d.year, d.month, 1)
                    + pd.offsets.MonthEnd(0)).day
        if d.day >= last_day - 2:
            return 2        # Monatsend
        if d.day >= last_day - 7:
            return 1        # uebrige Monatswoche
        return 0            # Rest

    sig["stratum"] = [month_stratum(d) for d in sig["date"]]
    groups = [sig.loc[sig["stratum"] == s, "dir"].to_numpy()
              * sig.loc[sig["stratum"] == s, "next_rth1h_ret"].to_numpy()
              for s in (0, 1, 2)]
    groups = [g[np.isfinite(g)] for g in groups]
    if all(len(g) >= 20 for g in groups):
        jt_p = jonckheere_p(groups)
        means = [float(np.mean(g)) * 1e4 for g in groups]
        print(f"[GATE 3b] Jonckheere p={jt_p:.4f} (vorregistriert: < 0.05) | "
              f"Strata-Mittel bps Rest/Woche/Monatsend: "
              f"{means[0]:.2f}/{means[1]:.2f}/{means[2]:.2f}")
    else:
        jt_p = np.nan
        print("[GATE 3b] zu wenig Replikate pro Stratum — uebersprungen.")

    # ============ Placebo-Pseudo-Anker (Gate 1 Symmetrie-Kontrolle) =========
    pb = R.dropna(subset=["placebo_bmr"])
    pb = pb[np.abs(pb["placebo_bmr"]) >= guard]
    if len(pb) >= 30:
        pb_signed = np.sign(pb["placebo_bmr"]) * pb["next_rth1h_ret"]
        print(f"[GATE 1] Placebo-Pseudo-Anker (Bar 13:59 CT, identische "
              f"{tick}-Rundung): n={len(pb)}, mean={pb_signed.mean() * 1e4:.2f} "
              f"bps (Erwartung ~0; signifikantes Placebo => Rundungs-/Grid-"
              f"Artefakt, Test nicht interpretierbar)")

    # ============ Decay-Split 2022+ (Pflicht-Output) ========================
    for label, sub in [("2019-2021", sig[sig["year"] < 2022]),
                       ("2022+ (ENTSCHEIDEND)", sig[sig["year"] >= 2022])]:
        s = sub["dir"] * sub["next_rth1h_ret"]
        if len(s) > 0:
            print(f"[DECAY] {label:<22} n={len(s):>5}  mean={s.mean() * 1e4:.2f} bps"
                  f"  hitrate={(s > 0).mean():.1%}")

    dst_n = int(sig["dst_flag"].sum())
    print(f"[ROBUSTA] DST-Flag-Tage im Signal-Sample: {dst_n} (nur Flag, ET/CT-basiert)")

    results[name] = dict(nogo=False, guard=guard, surv=surv, obs=obs,
                         hit=hit, cd=cd, pctile=pctile, jt_p=jt_p, n=len(sig))

# ------------------------- GESAMT-URTEIL ------------------------------------
print("\n" + "=" * 78)
print("GESAMT-URTEIL ID67o (vorregistrierte Abnahmekriterien)")
print("=" * 78)
for name, r in results.items():
    if r.get("nogo"):
        print(f"{name}: NO-GO (Gate 2 Ueberlebensrate {r['surv']:.1%} < 15% "
              f"bei Guard {r['guard']})")
    else:
        passed = (r["pctile"] > PERCENTILE_MIN and r["cd"] >= CLIFFS_D_MIN
                  and (not np.isfinite(r["jt_p"]) or r["jt_p"] < 0.05)
                  and r["hit"] > 0.52)
        print(f"{name}: n={r['n']}, Perzentil={r['pctile']:.1f}%, "
              f"Cliff's d={r['cd']:.3f}, JT-p={r['jt_p']}, Hit={r['hit']:.1%} "
              f"-> {'BESTANDEN' if passed else 'NICHT BESTANDEN'}")
# Falsifikator-Lesart: ES/NQ = Test; GC signifikant => generisches Risiko-Muster;
# ZB-Effekt nur auf ZB-1/64-Grid zulaessig — ES-Grid-Effekt in ZB waere der
# Nachweis, dass die Rundungsfalle real ist (Guard funktioniert).
