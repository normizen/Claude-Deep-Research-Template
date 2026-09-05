# =============================================================================
# ID41o — 0DTE-Close-Gamma-Reversions-Panel (TEST-ZELLE, QC Research Notebook)
# =============================================================================
# Vorab registriert (VOR Ausfuehrung, Datenfalle 5):
#   Umbau 1: ES + NQ = Test-Beine (echtes 16:00-0DTE-Gamma-Ende).
#            GC + ZB = Kontroll-/Falsifikator-Beine (kein homologes
#            0DTE-Ende — dort darf der Effekt NICHT auftreten).
#   Umbau 2: Nur oberes |GEX|-Quartil handelbar; Median-0DTE-Net-Gamma
#            traegt nichts. Dosis-Variable: Flip-Level-Naehe (ordinal).
#   Umbau 3: Overnight GESTRICHEN aus Kern-Hypothese. Kern-Zelle =
#            letzte ~30 RTH-Min vor Verfall-Close -> Reversion in den
#            letzten Minuten des Verfallstags selbst. Overnight nur als
#            explorative Nebenzeile, als eingepreist markiert.
#
# Signal (Kern):  Reversion = -sign(R_zwang) * R_reversion
#   R_zwang     = Close(15:30 ET) -> Close(16:00 ET)   [Zwangsphase, RTH]
#   R_reversion = Close(15:30 ET) -> Close(16:00 ET) im GEGEN-Test, d.h.
#                 Reversion IN den letzten RTH-Minuten: Erste-Haelfte vs.
#                 Letzte-Haelfte des 15:30-16:00-Fensters (ID26-V2-Logik):
#   R_erst   = 15:30 -> 15:45 ; R_letzt = 15:45 -> 16:00
#   Reversions-Score = -sign(R_erst) * R_letzt  (pro Tag, pro Bein)
# Explorativ (eingepreist markiert): R_16:00 -> Folgetag 09:30 (Overnight).
#
# Huertden (Abnahmekonvention, exakt wie ID26):
#   Cliff's d >= 0.10 auf Panel-Mittel (ES,NQ) UND Placebo-Perzentil > 95%
#   (500 Permutationen: Nicht-Verfallstage gleiche Uhrzeit).
#   Falsifikator: gleiche Staerke in GC/ZB -> REFUTED als Gamma-Effekt.
#   Decay-Split: Effekt 2022+ muss existieren, 2019-2021 NICHT
#   (0DTE jung; 2019-2021 = Kontrolle).
#
# Datenfallen eingehalten: 1 (continuous backadjusted, keine Roh-Mischung),
# 2 (Placebo Pflicht), 3 (keine Glaettung — Tageslevel |GEX|-Proxy),
# 4 (Abstain ausgeschlossen UND gezaehlt), 5 (Vorab-Registrierung oben).
#
# QB-GLOBAL: `qb` wird im QC-Notebook bereitgestellt — NICHT neu instanziieren.
# =============================================================================

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 0. Defensive Checks (qb-Global, kein Neubau)
# ---------------------------------------------------------------------------
try:
    qb
except NameError:
    raise RuntimeError(
        "qc_id41o: `qb`-Global fehlt — Zelle muss im QC Research "
        "Notebook laufen (QuantBook bereits vorhanden).")

print("=" * 78)
print("ID41o — 0DTE-CLOSE-GAMMA-REVERSIONS-PANEL (2+2-Design, Kern=RTH-Close)")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. Instrumente: 2 Test-Beine + 2 Kontroll-Beine
# ---------------------------------------------------------------------------
test_legs = {
    "ES": Futures.Indices.SP_500_E_MINI,
    "NQ": Futures.Indices.NASDAQ_100_E_MINI,
}
control_legs = {
    "GC": Futures.Metals.GOLD,
    "ZB": Futures.Financials.Y_30_TREASURY_BOND,  # BUGFIX run1: QC-Enum-Name
}

futures = {}
for ticker, market in {**test_legs, **control_legs}.items():
    fut = qb.add_future(
        market,
        data_mapping_mode=DataMappingMode.OPEN_INTEREST,
        data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO,
        extended_market_hours=True,   # BUGFIX (ID29-run1): ohne das endet die
        # History ~17:00 ET -> Overnight/explorative Fenster leer
    )
    futures[ticker] = fut
    print("add_future OK: {} -> {}".format(ticker, fut.symbol))

# ---------------------------------------------------------------------------
# 2. Zeitraum, ET, DST-Flag
# ---------------------------------------------------------------------------
start_all = datetime(2019, 1, 1)
end_all = datetime(2026, 8, 31)
et_tz = "America/New_York"

def is_dst_transition_day(d):
    """Flag: US-DST-Umstellungstage (2. So Maerz / 1. So November) — nur Flag."""
    month, day, wd = d.month, d.day, d.weekday()
    if month == 3 and 8 <= day <= 14 and wd == 6:
        return True
    if month == 11 and 1 <= day <= 7 and wd == 6:
        return True
    return False

# ---------------------------------------------------------------------------
# 3. Minuten-History pro Bein, strikt ET
# ---------------------------------------------------------------------------
bars = {}
for ticker, fut in futures.items():
    hist = qb.history(fut.symbol, start_all, end_all, Resolution.MINUTE,
                      extended_market_hours=True)  # BUGFIX: auch history-Call
    if hist.empty:
        raise RuntimeError("qc_id41o: leere History fuer " + ticker)
    df = hist.copy()
    # BUGFIX run2+3: qb.history liefert MultiIndex (z.B. (time, expiry) oder
    # (symbol, time)) — droplevel(0) allein reicht nicht immer. Robuster:
    # Index komplett auf die Zeit-Ebene reduzieren.
    if isinstance(df.index, pd.MultiIndex):
        # Zeit ist die Ebene mit Datetime-Werten — finde sie
        time_level = None
        for i, lvl in enumerate(df.index.levels):
            if pd.api.types.is_datetime64_any_dtype(lvl):
                time_level = i
                break
        if time_level is not None:
            df.index = df.index.get_level_values(time_level)
        else:
            # Fallback: letzte Ebene annehmen
            df.index = df.index.get_level_values(-1)
    # QC liefert UTC-Index -> strikt ET
    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    df.index = df.index.tz_convert(et_tz)
    df = df[~df.index.duplicated(keep="last")]
    bars[ticker] = df
    print("history OK: {}  bars={}  {} .. {}".format(
        ticker, len(df), df.index.min().date(), df.index.max().date()))

# ---------------------------------------------------------------------------
# 4. Fenster-Extraktion (ET): 15:30 / 15:45 / 16:00 (+ explorativ Overnight)
# ---------------------------------------------------------------------------
def last_close_at_or_before(df, d, hh, mm):
    """Letzter Close <= d hh:mm ET; None wenn fehlend/halber Tag."""
    target = pd.Timestamp(d).tz_localize(et_tz) + timedelta(hours=hh, minutes=mm)
    day_start = pd.Timestamp(d).tz_localize(et_tz)
    window = df.loc[(df.index >= day_start) & (df.index <= target), "close"]
    if window.empty:
        return None
    return float(window.iloc[-1])

def first_close_at_or_after(df, d, hh, mm):
    target = pd.Timestamp(d).tz_localize(et_tz) + timedelta(hours=hh, minutes=mm)
    day_end = target + timedelta(days=1)
    window = df.loc[(df.index >= target) & (df.index < day_end), "close"]
    if window.empty:
        return None
    return float(window.iloc[0])

# Abstain-Regeln (vorab registriert): Feiertage/halbe Tage = fehlende
# 15:30-16:00-Minuten; FOMC/CPI als Flag-Liste (hier: manuell leer = keine
# zusaetzlichen Abstains ausser Datenfehlern — im Protokoll gezaehlt).
fomc_cpi_days = set()  # vorregistrierte Ausnahmen hier eintragen

rows = []
all_days = sorted(set(
    d.normalize() for df in bars.values()
    for d in df.loc[df.index.time >= datetime.strptime("15:30", "%H:%M").time(),
                    "close"].index.normalize()))

print("Handelstage mit 15:30+-Daten (roh): {}".format(len(all_days)))

abstain_count = 0
dst_flag_count = 0
for d in all_days:
    date_d = d.date()
    dst_flag = is_dst_transition_day(pd.Timestamp(date_d))
    if dst_flag:
        dst_flag_count += 1
    if date_d in fomc_cpi_days:
        abstain_count += 1
        continue
    rec = {"date": date_d, "year": date_d.year,
           "weekday": date_d.weekday(), "dst_flag": dst_flag}
    ok = True
    for ticker, df in bars.items():
        c1530 = last_close_at_or_before(df, d, 15, 30)
        c1545 = last_close_at_or_before(df, d, 15, 45)
        c1600 = last_close_at_or_before(df, d, 16, 0)
        # halber Tag / Datenluecke -> Abstain (ausgeschlossen UND gezaehlt)
        if c1530 is None or c1545 is None or c1600 is None:
            ok = False
            break
        rec[ticker + "_r_erst"] = np.log(c1545 / c1530)
        rec[ticker + "_r_letzt"] = np.log(c1600 / c1545)
    if not ok:
        abstain_count += 1
        continue
    # explorativ, eingepreist markiert: Overnight ES
    es_df = bars["ES"]
    c1600_es = last_close_at_or_before(es_df, d, 16, 0)
    nxt = es_df.loc[es_df.index.normalize() > d, "close"]
    if len(nxt) > 0:
        first_next_day = nxt.index.normalize()[0]
        c930_next = first_close_at_or_after(es_df, first_next_day, 9, 30)
        if c930_next is not None and c1600_es is not None:
            rec["ES_r_overnight"] = np.log(c930_next / c1600_es)
    rows.append(rec)

panel = pd.DataFrame(rows).sort_values("date").reset_index(drop=True)
print("Abstain-Tage (ausgeschlossen UND gezaehlt): {} ({:.1f}%)".format(
    abstain_count, 100.0 * abstain_count / max(1, len(all_days))))
print("DST-Flag-Tage (nur Flag, ET-basiert): {}".format(dst_flag_count))
print("Tradable Tage im Panel: {}".format(len(panel)))

# ---------------------------------------------------------------------------
# 5. Umbau 2: oberes |GEX|-Quartil — handelbar-Filter
#    Proxy: taegliche Realisierung des Zwangsfensters als |GEX|-Surrogat
#    (QC liefert kein historisches MM-Net-Gamma kostenlos; Proxy =
#    |R_zwang| des Tages selbst ist LOOK-AHEAD -> verboten.
#    Stattdessen: rollierendes 20d-Median-|R_erst+R_letzt| VOR dem Tag,
#    oberes Quartil der rollierenden Verteilung = "hohes Gamma-Regime".)
# ---------------------------------------------------------------------------
panel["es_zwang"] = panel["ES_r_erst"] + panel["ES_r_letzt"]
panel["nq_zwang"] = panel["NQ_r_erst"] + panel["NQ_r_letzt"]
panel["zwang_abs"] = (panel["es_zwang"].abs() + panel["nq_zwang"].abs()) / 2.0
panel["gamma_regime"] = (
    panel["zwang_abs"].shift(1).rolling(60, min_periods=40).median())
q75 = panel["gamma_regime"].quantile(0.75)
panel["tradable"] = panel["gamma_regime"] >= q75
n_tradable = int(panel["tradable"].sum())
print("Oberes |GEX|-Proxy-Quartil (handelbar): {} Tage ({:.0f}%)".format(
    n_tradable, 100.0 * n_tradable / max(1, len(panel))))

# Dosis-Variable (ordinal): Flip-Level-Naehe-Proxy = Tages-Zwang relativ
# zum rollierenden Regime (0=fern ... 3=nah, Quartil-Bins, shift(1) =
# kein Look-Ahead)
panel["dose"] = pd.qcut(
    panel["zwang_abs"].shift(1).rolling(60, min_periods=40).rank(pct=True),
    4, labels=False)

# ---------------------------------------------------------------------------
# 6. Reversions-Score, Expiry-Filter (seit Mai 2022 taegliche SPX-Verfaelle;
#    davor Mo/Mi/Fr). Test nur auf Verfallstagen.
# ---------------------------------------------------------------------------
def is_expiry_day(d):
    dt = pd.Timestamp(d)
    if dt >= pd.Timestamp("2022-05-01"):
        return dt.weekday() < 5            # taegliche Verfaelle Mo-Fr
    return dt.weekday() in (0, 2, 4)       # Pre-2022: Mo/Mi/Fr

panel["expiry"] = panel["date"].map(is_expiry_day)
panel["decay_regime"] = np.where(panel["year"] >= 2022, "2022+", "2019-2021")

for leg in ["ES", "NQ", "GC", "ZB"]:
    panel[leg + "_rev"] = (
        -np.sign(panel[leg + "_r_erst"]) * panel[leg + "_r_letzt"])

sample = panel[panel["expiry"] & panel["tradable"]].dropna(
    subset=["ES_rev", "NQ_rev", "GC_rev", "ZB_rev"]).copy()
print("Analyse-Sample (Expiry & Top-Gamma-Quartil): n = {}".format(len(sample)))

# ---------------------------------------------------------------------------
# 7. Statistik: Cliff's d, Placebo (500 Permutationen, Nicht-Verfallstage
#    gleiche Uhrzeit), Decay-Split, 2+2-Falsifikator
# ---------------------------------------------------------------------------
def cliffs_delta(x, y):
    x = np.asarray(x); y = np.asarray(y)
    gt = sum((xi > y).sum() for xi in x)
    lt = sum((xi < y).sum() for xi in x)
    return (gt - lt) / float(len(x) * len(y))

test_rev = ((sample["ES_rev"] + sample["NQ_rev"]) / 2.0).values
ctrl_rev = ((sample["GC_rev"] + sample["ZB_rev"]) / 2.0).values

# Nullmodell: Reversions-Score auf Nicht-Verfallstagen (gleiche Uhrzeit,
# gleiche Instrumente, gleiches Gamma-Quartil)
null_pool = panel[~panel["expiry"] & panel["tradable"]].dropna(
    subset=["ES_rev", "NQ_rev"])
null_scores = ((null_pool["ES_rev"] + null_pool["NQ_rev"]) / 2.0).values

rng = np.random.default_rng(41)
n_perm = 500
perm_means = np.empty(n_perm)
for i in range(n_perm):
    k = min(len(test_rev), len(null_scores))
    perm_means[i] = rng.choice(null_scores, size=k, replace=False).mean()
placebo_pct = 100.0 * (perm_means < test_rev.mean()).mean()

d_vs_null = cliffs_delta(test_rev, rng.choice(
    null_scores, size=min(len(test_rev), len(null_scores)), replace=False))
d_test_vs_ctrl = cliffs_delta(test_rev, ctrl_rev)

print("\n[1] KERN-HYPOTHESE (ES+NQ, Expiry, oberes Gamma-Quartil):")
print("    n Test-Replikate:           {}".format(len(test_rev)))
print("    Mean Reversions-Score:      {:+.6f}".format(test_rev.mean()))
print("    Cliff's d vs. Null-Pool:    {:+.3f}   (Huerde >= 0.10)".format(
    d_vs_null))
print("    Placebo-Perzentil (n=500):  {:.1f}%   (Huerde > 95%)".format(
    placebo_pct))

print("\n[2] FALSIFIKATOR (GC+ZB Kontroll-Beine, darf NICHT auftreten):")
print("    Mean Kontroll-Score:        {:+.6f}".format(ctrl_rev.mean()))
print("    Cliff's d Test vs. Kontrolle: {:+.3f}".format(d_test_vs_ctrl))
print("    -> d(Test,Ctrl) > 0: Gamma-Kanal plausibel; ~0: generischer "
      "Close-Effekt = REFUTED")

print("\n[3] DECAY-SPLIT (0DTE jung — 2019-2021 darf NICHT existieren):")
for regime in ["2019-2021", "2022+"]:
    sub = sample[sample["decay_regime"] == regime]
    if len(sub) < 30:
        print("    {:9s}: n={} (zu klein)".format(regime, len(sub)))
        continue
    s = ((sub["ES_rev"] + sub["NQ_rev"]) / 2.0).values
    print("    {:9s}: n={:4d}  mean={:+.6f}  hitrate={:.1f}%".format(
        regime, len(s), s.mean(), 100.0 * (s > 0).mean()))

print("\n[4] DOSIS-RESPONSE (ordinal, Flip-Naehe-Proxy 0..3):")
for dose in range(4):
    sub = sample[sample["dose"] == dose]
    if len(sub) == 0:
        continue
    s = ((sub["ES_rev"] + sub["NQ_rev"]) / 2.0).values
    print("    Dosis {}: n={:4d}  mean={:+.6f}".format(dose, len(s), s.mean()))

print("\n[5] EXPLORATIV — Overnight (EINGEPREIST markiert, nicht Kern):")
ov = sample.dropna(subset=["ES_r_overnight"])
if len(ov) > 0:
    ov_score = (-np.sign(ov["es_zwang"]) * ov["ES_r_overnight"]).values
    print("    n={}  mean={:+.6f}  hitrate={:.1f}%  "
          "[generischer Close-Effekt, eingepreist — kein Gamma-Kanal]".format(
              len(ov_score), ov_score.mean(), 100.0 * (ov_score > 0).mean()))

print("\n[6] ID52k-METRIK — Bet-Hedging (geometrisches Mittel, regime-stratif.):")
for regime in ["2019-2021", "2022+"]:
    sub = sample[sample["decay_regime"] == regime]
    if len(sub) < 30:
        continue
    # Wett-Quote: Ertrag pro eingesetzter Risiko-Einheit (|R_zwang| als Einsatz)
    es_ret = sub["ES_rev"] / sub["es_zwang"].abs().clip(lower=1e-6)
    growth = (1.0 + es_ret.clip(lower=-0.99)).values
    geo = float(np.exp(np.log(growth).mean()) - 1.0)
    print("    {:9s}: geo-mean pro Replikat = {:+.4%}  (n={})".format(
        regime, geo, len(sub)))

print("\n" + "=" * 78)
print("URTEIL (vorregistrierte Huerden):")
passed = (d_vs_null >= 0.10) and (placebo_pct > 95.0) and (d_test_vs_ctrl > 0.0)
print("  Cliff's d >= 0.10:  {}".format("OK" if d_vs_null >= 0.10 else "FAIL"))
print("  Placebo > 95%:      {}".format("OK" if placebo_pct > 95.0 else "FAIL"))
print("  Falsifikator klar:  {}".format("OK" if d_test_vs_ctrl > 0 else "FAIL"))
print("  => ID41o-Kern: {}".format("BESTANDEN" if passed else "NICHT BESTANDEN"))
print("=" * 78)
