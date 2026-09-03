# ============================================================================
# QC ID26 — Zeitfenster-System: Fenster-Test (QuantConnect Research Notebook)
# ============================================================================
# Eine einzige, vollstaendig lauffaehige Zelle fuer das QC-Research-Notebook
# (QuantBook-Umgebung). In eine neue Zelle kopieren und ausfuehren.
#
# ----------------------------------------------------------------------------
# HYPOTHESE (vorregistriert, VOR Ausfuehrung fixiert — Datenfalle 5):
#   Ein einzelnes vorregistriertes 30-Min-Fenster (15:30-16:00 ET) traegt nach
#   Kosten ein besseres Kosten/Asymmetrie-Profil als der Rest des Tages;
#   getestet auf ES-Minutenbars.
#
# VORREGISTRIERTE VORHERSAGEN:
#   V1 (primaer, entscheidend): Kostenquote (RT-Kosten / mittlere Fenster-Range)
#       im Ziel-Fenster ist >= Faktor 3 NIEDRIGER als der Tagesmedian ueber alle
#       RTH-30-Min-Fenster.
#   V2 (explorativ, sekundaer): Erst-30-Min -> letzt-30-Min Momentum (Market
#       Intraday Momentum, Gao et al. 2018) mit Decay-Split: Segment 2022+ ist
#       das ENTSCHEIDENDE Segment. Erwartung laut gex.live-Replikation: flach.
#       Positiv 2019-2021 + flach 2022+ zaehlt als Decay-Bestaetigung, NICHT
#       als Signal-Erfolg.
#
# ABNAHMEKRITERIEN (vorab):
#   Effekt gilt NUR bei Cliff's d >= 0.10 UND oberhalb des 95%-Perzentils von
#   500 Placebo-Fenstern (zufaellige 30-Min-Fenster gleicher Stichprobenzahl).
#   Bei Nichterfuellung: Fenster-Hypothese tot — KEINE Neu-Fenster-Suche im
#   selben Datensatz (Datenfalle 5).
#
# DATENFALLEN-BEHANDLUNG:
#   Falle 1 (Preisreihen-Mix): QC continuous future, dataMappingMode=OPEN_INTEREST,
#       dataNormalizationMode=BACKWARDS_RATIO_ADJUSTED (backadjusted). Dokumentiert.
#       Keine Mischung mit Roh-Kontraktserien.
#   Falle 2 (kein Placebo): 500 zufaellige 30-Min-Fenster, siehe PLACEBO_N.
#   Falle 4 (kein Abstain): Tage mit Fenster-Volumen < VOLUME_MIN_SHARE des
#       Tagesvolumens-20d-Medians im Fenster werden ausgeschlossen UND gezaehlt.
#   DST-FALLE: Alle Zeiten strikt America/New_York (ET). US/EU-Sommerzeit weicht
#       2x jaehrlich 2-3 Wochen ab — NIEMALS in Lokalzeit rechnen. QC liefert
#       Bars bereits in Exchange-Zeitzone (ET); Tage in den DST-Übergangswochen
#       werden separat geflaggt (DST_FLAG), Ergebnis auch ohne sie berichtet.
# ============================================================================

import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta

# ------------------------- KONFIGURATION (vorregistriert) -------------------
SYMBOL          = Futures.Indices.SP500EMini
START           = datetime(2019, 1, 1)
END             = datetime(2026, 9, 1)
TARGET_WINDOW   = (time(15, 30), time(16, 0))      # ET — das vorregistrierte Fenster
FIRST_WINDOW    = (time(9, 30), time(10, 0))       # ET — erste 30 Min (Momentum)
RTH_OPEN        = time(9, 30)
RTH_CLOSE       = time(16, 0)
WIN_MINUTES     = 30
RT_COST_USD     = 13.50      # ES all-in Round-Trip (Kommission+Gebuehren+1 Tick Slippage)
ES_MULTIPLIER   = 50.0       # USD pro Punkt
PLACEBO_N       = 500
CLIFFS_D_MIN    = 0.10
PERCENTILE_MIN  = 95.0
COST_RATIO_FACTOR_MIN = 3.0
VOLUME_MIN_SHARE = 0.002     # Abstain: Fenster-Volumen < 0.2% des 20d-Median-Tagesvolumens -> Tag ausgeschlossen & gezaehlt
SEED            = 26         # reproduzierbar

rng = np.random.default_rng(SEED)

# ------------------------- DATEN (Datenfalle 1: dokumentiert) ---------------
future = qb.AddFuture(SYMBOL,
                      dataMappingMode=DataMappingMode.OpenInterest,
                      dataNormalizationMode=DataNormalizationMode.BackwardsRatioAdjusted,
                      dataAdjustmentMode=DataAdjustmentMode.NoAdjustment)
symbol = future.Symbol
print(f"Datenreihe: {symbol} | continuous, mapping=OpenInterest, "
      f"normalization=BackwardsRatioAdjusted (backadjusted) — KEINE Roh-Serien-Mischung")

history = qb.History(symbol, START, END, Resolution.Minute)
df = history.reset_index()
# QC liefert Futures-Bars in Exchange-Zeitzone = America/New_York (ET). DST-sicher.
df["time"] = pd.to_datetime(df["time"])
df["date"] = df["time"].dt.date
df["tod"]  = df["time"].dt.time

# ------------------------- DST-FLAG (Dokumentation, kein Filter) ------------
def in_dst_gap_weeks(d):
    """Wochen, in denen US- und EU-Sommerzeit asynchron sind (Maerz/Ende Okt-Anf Nov).
    Flag nur — Analyse laeuft strikt in ET, kein Lokalzeit-Bezug noetig."""
    m, day = d.month, d.day
    return (m == 3 and 8 <= day <= 31) or (m == 10 and day >= 25) or (m == 11 and day <= 7)

# ------------------------- FENSTER-EXTRAKTION -------------------------------
def window_bars(day_df, start_t, end_t):
    return day_df[(day_df["tod"] >= start_t) & (day_df["tod"] < end_t)]

def window_range_usd(bars):
    if len(bars) < WIN_MINUTES // 2:   # weniger als halbe Bars -> Fenster nicht handelbar
        return None, None
    rng_pts = bars["high"].max() - bars["low"].min()
    return rng_pts * ES_MULTIPLIER, bars["volume"].sum()

# Alle moeglichen RTH-30-Min-Fenster-Starts (9:30 .. 15:30)
slot_starts = []
t = datetime.combine(datetime(2000, 1, 1), RTH_OPEN)
while t.time() < RTH_CLOSE:
    slot_starts.append(t.time())
    t += timedelta(minutes=WIN_MINUTES)

days = sorted(df["date"].unique())
print(f"Handelstage gesamt: {len(days)}  ({days[0]} .. {days[-1]})")

# Tagesvolumen-20d-Median fuer Abstain-Schwelle
day_vol = df.groupby("date")["volume"].sum()
day_vol_med20 = day_vol.rolling(20, min_periods=5).median()

records = []
abstain_count = 0
for d in days:
    day_df = df[df["date"] == d]
    rec = {"date": d, "year": d.year, "dst_flag": in_dst_gap_weeks(d)}
    # Abstain-Logik (Datenfalle 4): Liquiditaet im Ziel-Fenster pruefen
    tb = window_bars(day_df, *TARGET_WINDOW)
    _, tv = window_range_usd(tb)
    med = day_vol_med20.get(d, np.nan)
    if tv is None or not np.isfinite(med) or tv < VOLUME_MIN_SHARE * med:
        abstain_count += 1
        rec["abstain"] = True
    else:
        rec["abstain"] = False
    # Ranges aller Slots
    for s in slot_starts:
        e = (datetime.combine(datetime(2000, 1, 1), s) + timedelta(minutes=WIN_MINUTES)).time()
        bars = window_bars(day_df, s, e)
        r, _ = window_range_usd(bars)
        rec[f"rng_{s.strftime('%H%M')}"] = r if r else np.nan
    # Momentum-Beine (explorativ)
    fw = window_bars(day_df, *FIRST_WINDOW)
    tw = tb
    if len(fw) >= WIN_MINUTES // 2 and len(tw) >= WIN_MINUTES // 2:
        rec["first_ret"] = fw["close"].iloc[-1] / fw["open"].iloc[0] - 1.0
        rec["last_ret"] = tw["close"].iloc[-1] / tw["open"].iloc[0] - 1.0
    records.append(rec)

R = pd.DataFrame(records)
target_col = "rng_1530"
tradable = R[~R["abstain"] & R[target_col].notna()].copy()
print(f"Abstain-Tage (Datenfalle 4, ausgeschlossen UND gezaehlt): {abstain_count} "
      f"({abstain_count/len(days):.1%}) — tradable Tage: {len(tradable)}")

# ------------------------- HILFSFUNKTIONEN ----------------------------------
def cliffs_delta(a, b):
    """Cliff's d: P(a>b) - P(a<b)."""
    a = np.asarray(a)[~np.isnan(a)]; b = np.asarray(b)[~np.isnan(b)]
    if len(a) == 0 or len(b) == 0: return np.nan
    gt = (a[:, None] > b[None, :]).sum()
    lt = (a[:, None] < b[None, :]).sum()
    return (gt - lt) / (len(a) * len(b))

# ------------------------- V1: KOSTENQUOTE-ASYMMETRIE -----------------------
range_cols = [f"rng_{s.strftime('%H%M')}" for s in slot_starts]
tradable["median_other_range"] = tradable[[c for c in range_cols if c != target_col]].median(axis=1)
cost_ratio_target = RT_COST_USD / tradable[target_col]
cost_ratio_others = RT_COST_USD / tradable["median_other_range"]

asymmetry_factor = cost_ratio_others.median() / cost_ratio_target.median()
cd_cost = cliffs_delta(cost_ratio_others.values, cost_ratio_target.values)

# Placebo: 500 zufaellige 30-Min-Fenster (Datenfalle 2) — ziehe je Ziehung
# ein zufaelliges Nicht-Ziel-Fenster und rechne dessen Asymmetrie-Faktor
placebo_factors = []
other_cols = [c for c in range_cols if c != target_col]
n_days = len(tradable)
for _ in range(PLACEBO_N):
    pc = rng.choice(other_cols)
    pr = RT_COST_USD / tradable[pc]
    po = RT_COST_USD / tradable[[c for c in range_cols if c != pc]].median(axis=1)
    placebo_factors.append(po.median() / pr.median())
placebo_factors = np.array(placebo_factors)
pctile = 100.0 * (placebo_factors < asymmetry_factor).mean()

# ------------------------- V2: MOMENTUM (explorativ) + DECAY-SPLIT ----------
def momentum_stats(sub):
    sub = sub.dropna(subset=["first_ret", "last_ret"])
    if len(sub) < 30: return dict(n=len(sub), corr=np.nan, hitrate=np.nan)
    c = np.corrcoef(sub["first_ret"], sub["last_ret"])[0, 1]
    hit = (np.sign(sub["first_ret"]) == np.sign(sub["last_ret"])).mean()
    return dict(n=len(sub), corr=c, hitrate=hit)

mom_all    = momentum_stats(tradable)
mom_pre22  = momentum_stats(tradable[tradable["year"] < 2022])
mom_22plus = momentum_stats(tradable[tradable["year"] >= 2022])   # ENTSCHEIDENDES Segment

# ------------------------- OUTPUT -------------------------------------------
print("\n" + "=" * 78)
print("ERGEBNIS ID26 — FENSTER-TEST (ES, 2019-2026, continuous backadjusted, ET)")
print("=" * 78)

print("\n[1] Kostenquote pro RTH-30-Min-Fenster (RT ${:.2f} / mittlere Fenster-Range):".format(RT_COST_USD))
tbl = []
for s in slot_starts:
    c = f"rng_{s.strftime('%H%M')}"
    med_rng = tradable[c].median()
    mark = "  <-- ZIEL" if c == target_col else ""
    tbl.append((f"{s.strftime('%H:%M')}-{(datetime.combine(datetime(2000,1,1),s)+timedelta(minutes=30)).strftime('%H:%M')}",
                med_rng, RT_COST_USD / med_rng if med_rng and med_rng > 0 else np.nan, mark))
tbl_df = pd.DataFrame(tbl, columns=["Fenster (ET)", "Median-Range $", "Kostenquote", ""])
tbl_df["Kostenquote"] = tbl_df["Kostenquote"].map(lambda x: f"{x:.1%}" if np.isfinite(x) else "n/a")
tbl_df["Median-Range $"] = tbl_df["Median-Range $"].map(lambda x: f"{x:,.0f}" if np.isfinite(x) else "n/a")
print(tbl_df.to_string(index=False))

print(f"\n[2] V1 — Kostenquote-Asymmetrie (Ziel-Fenster vs. Tagesmedian):")
print(f"    Asymmetrie-Faktor:           {asymmetry_factor:.2f}x   (vorregistriert: >= {COST_RATIO_FACTOR_MIN:.0f}x)")
print(f"    Cliff's d:                   {cd_cost:.3f}    (vorregistriert: >= {CLIFFS_D_MIN})")
print(f"    Placebo-Perzentil (n={PLACEBO_N}):   {pctile:.1f}%    (vorregistriert: > {PERCENTILE_MIN:.0f}%)")
v1_pass = (asymmetry_factor >= COST_RATIO_FACTOR_MIN and cd_cost >= CLIFFS_D_MIN and pctile > PERCENTILE_MIN)
print(f"    => V1 {'BESTANDEN' if v1_pass else 'NICHT BESTANDEN — Fenster-Hypothese tot, keine Neu-Suche (Datenfalle 5)'}")

print(f"\n[3] V2 — Erst-30-Min -> Letzt-30-Min Momentum (explorativ):")
for name, m in [("2019-2026 gesamt", mom_all), ("2019-2021", mom_pre22), ("2022+ (ENTSCHEIDEND)", mom_22plus)]:
    print(f"    {name:<24} n={m['n']:>5}  corr={m['corr']:+.4f}  hitrate={m['hitrate']:.1%}")
decay_confirmed = (np.isfinite(mom_22plus["corr"]) and mom_22plus["corr"] <= 0.02
                   and np.isfinite(mom_pre22["corr"]) and mom_pre22["corr"] > mom_22plus["corr"])
print(f"    => Decay-Befund (gex.live konsistent): {'JA' if decay_confirmed else 'NEIN/UNKLAR'}")

print(f"\n[4] Robusta: Abstain-Tage = {abstain_count} | DST-Flag-Tage = {int(R['dst_flag'].sum())} "
      f"(nur Flag, ET-basiert)")
no_dst = tradable[~tradable["dst_flag"]]
if len(no_dst) > 100:
    af2 = (RT_COST_USD / no_dst[[c for c in range_cols if c != target_col]].median(axis=1)).median() / \
          (RT_COST_USD / no_dst[target_col]).median()
    print(f"    Asymmetrie-Faktor ohne DST-Uebergangstage: {af2:.2f}x (Robustheitscheck)")
print("=" * 78)
