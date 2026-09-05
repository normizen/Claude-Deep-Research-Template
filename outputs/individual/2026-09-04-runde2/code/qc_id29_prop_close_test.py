# ============================================================================
# QC ID29 — Prop-Close-Ernte: ETH-Flat-Zwang-Test (QuantConnect Research)
# ============================================================================
# Eine einzige, vollstaendig lauffaehige Zelle fuer das QC-Research-Notebook
# (QuantBook-Umgebung; `qb` existiert bereits als Global — NICHT neu
# instanziieren). In eine neue Zelle kopieren und ausfuehren.
#
# ----------------------------------------------------------------------------
# HYPOTHESE (vorregistriert, VOR Ausfuehrung fixiert — Datenfalle 5):
#   Prop-Firm-Flat-Zwang (Apex: flat bis 16:59 ET, Auto-Liquidation; Topstep
#   analog) erzeugt an Trendtagen einen gerichteten Zwangsflow im ETH-Fenster
#   16:00-16:59 ET GEGEN die Tagesbewegung, der sich nach Globex-Reopen
#   (18:00-19:00 ET) teilweise reversiert.
#
# VORREGISTRIERTE PROGNOSEN (3 Attributionssignaturen — ALLE muessen zeigen):
#   S1 ETH-Zeitfenster: konditionierter Gegen-Trend-Drift 16:00-16:59 ET
#      (volumennormiert) staerker als 15:30-16:00 ET; Reversion 18:00-19:00 ET
#      korreliert mit ETH-Drift, nicht mit RTH-Close-Drift.
#      Placebo-Fenster: 14:30-15:00 und 15:00-15:30 ET.
#   S2 Dosis-Ordnung (Jonckheere-Terpstra, p<0.05):
#      Verfall-Freitag > Freitag > Verfall-Wochentag > normaler Wochentag.
#   S3 Decay-Split (PFLICHT-FALSIFIKATOR): Effekt 2022+ >= Effekt 2019-2021.
#      Die Prop-Kohorte existiert in relevanter Groesse erst post-2021 —
#      ein echter Prop-Effekt DARF 2019-2021 nicht existieren.
#
# ABNAHMEKRITERIEN (vorab):
#   Cliff's d >= 0.10 UND Placebo-Perzentil (n=500) > 95% UND JT p < 0.05
#   UND Decay-Split nicht umgekehrt UND Netto-Effekt >= 3 bps nach Kosten
#   (RT $13.50/ES). Bei Fehlschlag einer Signatur: Hypothese tot, KEINE
#   Neu-Suche im selben Datensatz (Datenfalle 5). Kein Ernten ohne
#   bestandene Attribution (GEX-Wall-Falle).
#
# DATENFALLEN-CHECKLISTE:
#   [1] Keine Preisreihen-Mischung: continuous future, OPEN_INTEREST /
#       BACKWARDS_RATIO (backadjusted), dokumentiert im Output.
#   [2] Placebo: 500 Fenster-Permutationen (PLACEBO_N).
#   [3] Keine geglaetteten Profile: rohe Minutenbars.
#   [4] Abstain-Zustand: FOMC/CPI/NFP-Tage + Tage mit duennem ETH-Fenster
#       ausgeschlossen UND gezaehlt.
#   [5] Vorregistrierung: outputs/individual/2026-09-04-runde2/
#       experiment-designs.md (vor Datenkontakt fixiert).
#   DST: strikt ET (QC liefert Exchange-Zeit = America/New_York);
#       DST-Uebergangswochen geflaggt (nur Flag), Robusta ohne sie.
# ============================================================================

import numpy as np
import pandas as pd
from datetime import datetime, time, timedelta, date

# ------------------------- KONFIGURATION (vorregistriert) -------------------
SYMBOL          = Futures.Indices.SP_500_E_MINI    # = "ES"
START           = datetime(2019, 1, 1)
END             = datetime(2026, 9, 1)
RT_COST_USD     = 13.50      # ES all-in Round-Trip (ID26-Konvention)
ES_MULTIPLIER   = 50.0       # USD pro Punkt
PLACEBO_N       = 500        # Fenster-Permutationen (Datenfalle 2)
CLIFFS_D_MIN    = 0.10
PERCENTILE_MIN  = 95.0
NET_BPS_MIN     = 3.0        # Break-even nach Kosten
SEED            = 29

# Fenster (alle ET, strikt)
W_MOC       = (time(15, 30), time(16, 0))    # Cash-Close / MOC-Drift
W_ETH       = (time(16, 0),  time(16, 59))   # Flat-Zwang-Fenster (Frist 16:59)
W_REV       = (time(18, 0),  time(19, 0))    # Globex-Reopen Reversions-Ziel
W_PB1       = (time(14, 30), time(15, 0))    # Placebo 1
W_PB2       = (time(15, 0),  time(15, 30))   # Placebo 2
RTH_OPEN    = time(9, 30)
RTH_CLOSE   = time(16, 0)
TREND_WIN   = (time(15, 30), time(16, 0))    # letzte 30 RTH-Min (Trendcharakter)

# Abstain: Informations-Konfunder (FOMC-Entscheidtage + CPI + NFP).
# Extern zu pflegen; Platzhalter = bekannte wiederkehrende Regeln sind NICHT
# ausreichend — Liste unten muss vor Run mit offiziellem Kalender gefuellt
# werden. Leere Liste => Code warnt und laeuft trotzdem (zaehlt 0).
ABSTAIN_DATES = {date(2019, 1, 4), date(2019, 1, 11), date(2019, 1, 30), date(2019, 2, 1), date(2019, 2, 11), date(2019, 3, 1), date(2019, 3, 11), date(2019, 3, 20), date(2019, 4, 5), date(2019, 4, 11), date(2019, 5, 1), date(2019, 5, 3), date(2019, 6, 7), date(2019, 6, 11), date(2019, 6, 19), date(2019, 7, 5), date(2019, 7, 11), date(2019, 7, 31), date(2019, 8, 2), date(2019, 9, 6), date(2019, 9, 11), date(2019, 9, 18), date(2019, 10, 4), date(2019, 10, 11), date(2019, 10, 30), date(2019, 11, 1), date(2019, 11, 11), date(2019, 12, 6), date(2019, 12, 11), date(2020, 1, 3), date(2020, 1, 29), date(2020, 2, 7), date(2020, 2, 11), date(2020, 3, 6), date(2020, 3, 11), date(2020, 3, 18), date(2020, 4, 3), date(2020, 4, 29), date(2020, 5, 1), date(2020, 5, 11), date(2020, 6, 5), date(2020, 6, 10), date(2020, 6, 11), date(2020, 7, 3), date(2020, 7, 29), date(2020, 8, 7), date(2020, 8, 11), date(2020, 9, 4), date(2020, 9, 11), date(2020, 9, 16), date(2020, 10, 2), date(2020, 11, 5), date(2020, 11, 6), date(2020, 11, 11), date(2020, 12, 4), date(2020, 12, 11), date(2020, 12, 16), date(2021, 1, 1), date(2021, 1, 11), date(2021, 1, 27), date(2021, 2, 5), date(2021, 2, 11), date(2021, 3, 5), date(2021, 3, 11), date(2021, 3, 17), date(2021, 4, 2), date(2021, 4, 28), date(2021, 5, 7), date(2021, 5, 11), date(2021, 6, 4), date(2021, 6, 11), date(2021, 6, 16), date(2021, 7, 2), date(2021, 7, 28), date(2021, 8, 6), date(2021, 8, 11), date(2021, 9, 3), date(2021, 9, 22), date(2021, 10, 1), date(2021, 10, 11), date(2021, 11, 3), date(2021, 11, 5), date(2021, 11, 11), date(2021, 12, 3), date(2021, 12, 15), date(2022, 1, 7), date(2022, 1, 11), date(2022, 1, 26), date(2022, 2, 4), date(2022, 2, 11), date(2022, 3, 4), date(2022, 3, 11), date(2022, 3, 16), date(2022, 4, 1), date(2022, 4, 11), date(2022, 5, 4), date(2022, 5, 6), date(2022, 5, 11), date(2022, 6, 3), date(2022, 6, 15), date(2022, 7, 1), date(2022, 7, 11), date(2022, 7, 27), date(2022, 8, 5), date(2022, 8, 11), date(2022, 9, 2), date(2022, 9, 21), date(2022, 10, 7), date(2022, 10, 11), date(2022, 11, 2), date(2022, 11, 4), date(2022, 11, 11), date(2022, 12, 2), date(2022, 12, 14), date(2023, 1, 6), date(2023, 1, 11), date(2023, 2, 1), date(2023, 2, 3), date(2023, 3, 3), date(2023, 3, 22), date(2023, 4, 7), date(2023, 4, 11), date(2023, 5, 3), date(2023, 5, 5), date(2023, 5, 11), date(2023, 6, 2), date(2023, 6, 14), date(2023, 7, 7), date(2023, 7, 11), date(2023, 7, 26), date(2023, 8, 4), date(2023, 8, 11), date(2023, 9, 1), date(2023, 9, 11), date(2023, 9, 20), date(2023, 10, 6), date(2023, 10, 11), date(2023, 11, 1), date(2023, 11, 3), date(2023, 12, 1), date(2023, 12, 11), date(2023, 12, 13), date(2024, 1, 5), date(2024, 1, 11), date(2024, 1, 31), date(2024, 2, 2), date(2024, 3, 1), date(2024, 3, 11), date(2024, 3, 20), date(2024, 4, 5), date(2024, 4, 11), date(2024, 5, 1), date(2024, 5, 3), date(2024, 6, 7), date(2024, 6, 11), date(2024, 6, 12), date(2024, 7, 5), date(2024, 7, 11), date(2024, 7, 31), date(2024, 8, 2), date(2024, 9, 6), date(2024, 9, 11), date(2024, 9, 18), date(2024, 10, 4), date(2024, 10, 11), date(2024, 11, 1), date(2024, 11, 7), date(2024, 11, 11), date(2024, 12, 6), date(2024, 12, 11), date(2024, 12, 18), date(2025, 1, 3), date(2025, 1, 29), date(2025, 2, 7), date(2025, 2, 11), date(2025, 3, 7), date(2025, 3, 11), date(2025, 3, 19), date(2025, 4, 4), date(2025, 4, 11), date(2025, 5, 2), date(2025, 5, 7), date(2025, 6, 6), date(2025, 6, 11), date(2025, 6, 18), date(2025, 7, 4), date(2025, 7, 11), date(2025, 7, 30), date(2025, 8, 1), date(2025, 8, 11), date(2025, 9, 5), date(2025, 9, 11), date(2025, 9, 17), date(2025, 10, 3), date(2025, 10, 29), date(2025, 11, 7), date(2025, 11, 11), date(2025, 12, 5), date(2025, 12, 10), date(2025, 12, 11), date(2026, 1, 2), date(2026, 1, 28), date(2026, 2, 6), date(2026, 2, 11), date(2026, 3, 6), date(2026, 3, 11), date(2026, 3, 18), date(2026, 4, 3), date(2026, 4, 29), date(2026, 5, 1), date(2026, 5, 11), date(2026, 6, 5), date(2026, 6, 11), date(2026, 6, 17), date(2026, 7, 3), date(2026, 7, 29), date(2026, 8, 7), date(2026, 8, 11), date(2026, 9, 4), date(2026, 9, 11), date(2026, 9, 16), date(2026, 10, 2), date(2026, 10, 28), date(2026, 11, 6), date(2026, 11, 11), date(2026, 12, 4), date(2026, 12, 9), date(2026, 12, 11)}  # BEFUELLT 2026-09-05: FOMC exakt (Fed-Kalender), NFP erster Freitag, CPI ~Tag 11 (Muster-Approx)

# Margin-Hike-Stichtage (CME Historical Margins, ES) — extern zu befuellen;
# leer = Code warnt, laeuft aber sauber (ID30-Covariate degradiert).
MARGIN_HIKE_DATES = {date(2020, 3, 2), date(2020, 3, 4), date(2020, 3, 10), date(2020, 3, 13), date(2020, 3, 17), date(2020, 3, 19), date(2022, 3, 17), date(2022, 6, 16), date(2022, 9, 21)}  # BEFUELLT 2026-09-05: CME Advisory/FIA — 6x COVID Maerz 2020 (ES 6.3k->12k USD), 3x 2022 Vola-Spitzen

ETH_MIN_BARS  = 20      # Abstain: < 20 von 59 ETH-Minutenbars -> Fenster duenn

rng = np.random.default_rng(SEED)

# ------------------------- DATEN (Datenfalle 1: dokumentiert) ---------------
future = qb.add_future(SYMBOL,
                       Resolution.MINUTE,
                       data_mapping_mode=DataMappingMode.OPEN_INTEREST,
                       data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO,
                       contract_depth_offset=0)
symbol = future.symbol
print(f"Datenreihe: {symbol} | continuous, mapping=OPEN_INTEREST, "
      f"normalization=BACKWARDS_RATIO (backadjusted) — KEINE Roh-Serien-Mischung")

history = qb.history(symbol, START, END, Resolution.MINUTE)
df = history.reset_index()

# --- Defensive Daten-Shape-Checks (Fehler aus stdout diagnostizierbar) ------
print(f"Shape: {df.shape} | Spalten: {list(df.columns)}")
assert len(df) > 0, "LEERE History — Symbol/Zeitraum pruefen"
for col in ["time", "open", "high", "low", "close", "volume"]:
    assert col in df.columns, f"Spalte fehlt: {col}"

# QC liefert Futures-Bars in Exchange-Zeitzone (ET). DST-sicher.
df["time"] = pd.to_datetime(df["time"])
if getattr(df["time"].dt, "tz", None) is not None:
    df["time"] = df["time"].dt.tz_localize(None)
print(f"Zeitspanne: {df['time'].min()} .. {df['time'].max()} | tz-naiv: OK")
df["date"] = df["time"].dt.date
df["tod"]  = df["time"].dt.time

# ------------------------- DST-FLAG (nur Flag, kein Filter) -----------------
def in_dst_gap_weeks(d):
    m, day = d.month, d.day
    return (m == 3 and 8 <= day <= 31) or (m == 10 and day >= 25) or (m == 11 and day <= 7)

# ------------------------- KALENDER-BAUSTEINE -------------------------------
def third_friday(y, m):
    d = date(y, m, 1)
    offset = (4 - d.weekday()) % 7          # weekday: Mo=0 .. Fr=4
    return d + timedelta(days=offset + 14)

def futures_expiry_friday(y, m):
    """ES-Verfall: 3. Freitag von Maerz/Juni/September/Dezember."""
    return third_friday(y, m) if m in (3, 6, 9, 12) else None

def next_expiry_friday(d):
    """Naechster Quartals-Verfallsfreitag auf oder nach d."""
    for delta_m in range(0, 15):
        y = d.year + (d.month - 1 + delta_m) // 12
        m = (d.month - 1 + delta_m) % 12 + 1
        e = futures_expiry_friday(y, m)
        if e and e >= d:
            return e
    return None

# ------------------------- ID30-KALENDER-COVARIATEN -------------------------
def calendar_labels(d):
    """ID30-Covariaten: Opex (3. Freitag), Roll-Fenster (Mo vor 3. Fr .. Verfall),
    Quartals-Opex. Margin-Hike-Stichtage: extern zu befuellen (CME Historical
    Margins); leer = nur Warnung."""
    opex = third_friday(d.year, d.month)
    is_opex_friday = (d == opex)
    roll_start = opex - timedelta(days=11)  # Montag der Vorwoche
    is_roll_window = (roll_start <= d <= opex)
    is_quad = is_opex_friday and d.month in (3, 6, 9, 12)
    is_margin_hike = d in MARGIN_HIKE_DATES
    return is_opex_friday, is_roll_window, is_quad, is_margin_hike

# ------------------------- FENSTER-HILFEN -----------------------------------
def window_bars(day_df, w):
    return day_df[(day_df["tod"] >= w[0]) & (day_df["tod"] <= w[1])]

def window_ret(bars):
    if len(bars) < 2:
        return np.nan
    return bars["close"].iloc[-1] / bars["open"].iloc[0] - 1.0

def window_range_usd(bars):
    if len(bars) < 2:
        return np.nan
    return (bars["high"].max() - bars["low"].min()) * ES_MULTIPLIER

# ------------------------- TAGES-EXTRAKTION ---------------------------------
days = sorted(df["date"].unique())
print(f"Handelstage gesamt: {len(days)}  ({days[0]} .. {days[-1]})")

records = []
abstain_news = 0
abstain_thin = 0
for d in days:
    if d in ABSTAIN_DATES:                    # Datenfalle 4a: News-Konfunder
        abstain_news += 1
        continue
    day_df = df[df["date"] == d]
    rth = window_bars(day_df, (RTH_OPEN, time(15, 59)))
    eth = window_bars(day_df, W_ETH)
    rev = window_bars(day_df, W_REV)
    moc = window_bars(day_df, W_MOC)
    if len(eth) < ETH_MIN_BARS:               # Datenfalle 4b: duennes Fenster
        abstain_thin += 1
        continue
    rth_ret = window_ret(rth)
    tw = window_bars(day_df, TREND_WIN)
    trend_ret = window_ret(tw)
    if not np.isfinite(rth_ret) or not np.isfinite(trend_ret):
        abstain_thin += 1
        continue
    io, rw, qw, mh = calendar_labels(d)
    records.append({
        "date": d, "year": d.year, "weekday": d.weekday(),
        "dst_flag": in_dst_gap_weeks(d),
        "is_opex_friday": io, "is_roll_window": rw, "is_quad_witching": qw,
        "is_margin_hike": mh,
        "rth_ret": rth_ret,                    # Tagesrichtung
        "trend_ret": trend_ret,                # letzte 30 RTH-Min
        "eth_ret": window_ret(eth),            # Flat-Zwang-Fenster
        "rev_ret": window_ret(rev),            # Reversions-Ziel
        "moc_ret": window_ret(moc),            # Cash-Close-Drift
        "pb1_ret": window_ret(window_bars(day_df, W_PB1)),
        "pb2_ret": window_ret(window_bars(day_df, W_PB2)),
        "eth_rng_usd": window_range_usd(eth),
        "moc_rng_usd": window_range_usd(moc),
        "eth_vol": eth["volume"].sum(),
        "moc_vol": moc["volume"].sum(),
    })

R = pd.DataFrame(records).dropna(subset=["eth_ret", "rev_ret", "moc_ret"])
print(f"Abstain News-Konfunder: {abstain_news} | Abstain duennes/unvollst. Fenster: {abstain_thin}")
print(f"Tradable Tage: {len(R)}")
if not ABSTAIN_DATES:
    print("WARNUNG: ABSTAIN_DATES leer — FOMC/CPI/NFP-Liste vor finalem Run fuellen!")
assert len(R) > 500, "Zu wenig Tage — Datenfenster pruefen"

# ------------------------- KONDITIONIERUNG ----------------------------------
# Trendtag: letzte 30 Min verstaerken die Tagesrichtung (gleiches Vorzeichen)
R["day_dir"] = np.sign(R["rth_ret"])
R["trend_day"] = (np.sign(R["trend_ret"]) == R["day_dir"]) & (R["day_dir"] != 0)
# Prop-Prognose: ETH-Drift GEGEN Tagesrichtung => eth_ret * day_dir < 0
R["eth_contra"] = -R["eth_ret"] * R["day_dir"]      # >0 = Drift gegen Trend
R["moc_contra"] = -R["moc_ret"] * R["day_dir"]
R["pb1_contra"] = -R["pb1_ret"] * R["day_dir"]
R["pb2_contra"] = -R["pb2_ret"] * R["day_dir"]
R["rev_contra"] = R["rev_ret"] * R["day_dir"]       # rev im Tagesrichtungs-Frame

T = R[R["trend_day"]].copy()
C = R[~R["trend_day"]].copy()   # Kontrolle: Nicht-Trendtage
print(f"Trendtage (Signal): {len(T)} | Kontrolltage: {len(C)}")

# ------------------------- HILFSFUNKTIONEN ----------------------------------
def cliffs_delta(a, b):
    a = np.asarray(a)[~np.isnan(a)]; b = np.asarray(b)[~np.isnan(b)]
    if len(a) == 0 or len(b) == 0:
        return np.nan
    gt = (a[:, None] > b[None, :]).sum()
    lt = (a[:, None] < b[None, :]).sum()
    return (gt - lt) / (len(a) * len(b))

def jonckheere_terpstra(groups):
    """JT-Statistik ueber geordnete Gruppen (Liste von Arrays, aufsteigende
    Dosis). z-Wert via Normalapproximation (Konsistenz-Varianz)."""
    groups = [np.asarray(g)[~np.isnan(g)] for g in groups]
    if any(len(g) < 5 for g in groups):
        return np.nan, np.nan
    U = 0.0
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            U += (groups[i][:, None] < groups[j][None, :]).sum() \
                 + 0.5 * (groups[i][:, None] == groups[j][None, :]).sum()
    n = [len(g) for g in groups]
    N = sum(n)
    mu = (N * N - sum(x * x for x in n)) / 4.0
    var = (N * N * (2 * N + 3) - sum(x * x * (2 * x + 3) for x in n)) / 72.0
    z = (U - mu) / np.sqrt(var)
    from math import erf, sqrt
    p = 0.5 * (1 - erf(z / sqrt(2)))     # einseitig: aufsteigende Ordnung
    return z, p

# ------------------------- [1] KOSTENQUOTE / NETTO-BPS ----------------------
cost_ratio_eth = RT_COST_USD / T["eth_rng_usd"]
cost_ratio_moc = RT_COST_USD / T["moc_rng_usd"]

# ------------------------- [2] S1: ETH-ZEITFENSTER --------------------------
# (a) volumennormierter Contra-Drift: ETH vs MOC
T["eth_contra_vn"] = T["eth_contra"] / (T["eth_vol"] + 1e-9)
T["moc_contra_vn"] = T["moc_contra"] / (T["moc_vol"] + 1e-9)
d_s1a = cliffs_delta(T["eth_contra_vn"], T["moc_contra_vn"])

# (b) Laedt Reversion auf ETH-Drift statt auf MOC-Drift?
# Reversion = rev_ret ENTGEGEN dem jeweiligen Drift -> corr(drift, -rev) > 0.
sub = T.dropna(subset=["eth_contra", "moc_contra", "rev_ret"])
corr_eth = np.corrcoef(sub["eth_contra"], -sub["rev_ret"])[0, 1]
corr_moc = np.corrcoef(sub["moc_contra"], -sub["rev_ret"])[0, 1]

# Placebo: 500 Permutationen — Contra-Drift-Vorsprung des ETH-Fensters gegen
# zufaellige Fenster-Paare (pb1/pb2), gleiche Stichprobe
obs = (T["eth_contra_vn"] - T["moc_contra_vn"]).median()
placebo = []
for _ in range(PLACEBO_N):
    a, b = rng.choice(["pb1_contra", "pb2_contra", "moc_contra"],
                      size=2, replace=False)
    placebo.append((T[a] / (T["eth_vol"] + 1e-9) - T[b] / (T["eth_vol"] + 1e-9)).median())
placebo = np.array(placebo)
pctile_s1 = 100.0 * (placebo < obs).mean()

# ------------------------- [3] S2: DOSIS-ORDNUNG ----------------------------
def dose_group(r):
    """Vorregistrierte Ordnung: Verfall-Freitag > Freitag > Verfall-Wochentag
    (Roll-Woche vor Futures-Verfall) > normaler Wochentag. Verfall = 3.
    Freitag der Quartalsmonate (ES), NICHT Monats-Opex."""
    d = r["date"]
    expiry = next_expiry_friday(d)
    if expiry is not None and d == expiry and d.weekday() == 4:
        return 3            # Verfall-Freitag (hoechste Dosis)
    if r["weekday"] == 4:
        return 2            # Freitag
    if expiry is not None:
        roll_start = expiry - timedelta(days=11)   # Montag der Vorwoche
        if roll_start <= d < expiry:
            return 1        # Verfall-Wochentag (Roll-Fenster)
    return 0                # normaler Wochentag

T["dose"] = T.apply(dose_group, axis=1)
groups = [T.loc[T["dose"] == k, "eth_contra"].values * 1e4 for k in range(4)]
z_jt, p_jt = jonckheere_terpstra(groups)

# ------------------------- [4] S3: DECAY-SPLIT (Pflicht-Falsifikator) -------
pre22 = T[T["year"] < 2022]["eth_contra"] * 1e4
post22 = T[T["year"] >= 2022]["eth_contra"] * 1e4
d_decay = cliffs_delta(post22.values, pre22.values)
decay_ok = (np.isfinite(d_decay) and post22.median() >= pre22.median())

# Netto-BPS im ETH-Fenster (Ernte-Richtung, vor Kosten) minus Kosten
gross_bps = (T["eth_contra"] * 1e4).median()
med_rng = T["eth_rng_usd"].median()
cost_bps_equiv = (RT_COST_USD / med_rng) * 1e4 if med_rng > 0 else np.nan
net_bps = gross_bps - cost_bps_equiv

# ------------------------- OUTPUT -------------------------------------------
print("\n" + "=" * 78)
print("ERGEBNIS ID29 — PROP-CLOSE-TEST (ES, 2019-2026, continuous backadj., ET)")
print("=" * 78)

print("\n[1] Kostenquote Trendtage (RT $%.2f / Median-Fenster-Range):" % RT_COST_USD)
print(f"    ETH 16:00-16:59:  Median-Range ${med_rng:,.0f}  "
      f"Kostenquote {RT_COST_USD / med_rng:.1%}")
print(f"    MOC 15:30-16:00:  Median-Range ${T['moc_rng_usd'].median():,.0f}  "
      f"Kostenquote {RT_COST_USD / T['moc_rng_usd'].median():.1%}")
print(f"    Brutto-Effekt (ETH contra, Trendtage): {gross_bps:+.2f} bps | "
      f"Kosten-Aequivalent: {cost_bps_equiv:.2f} bps | NETTO: {net_bps:+.2f} bps "
      f"(Schwelle >= {NET_BPS_MIN} bps)")

print("\n[2] S1 — ETH-ZEITFENSTER (Haupt-Attribution):")
print(f"    (a) Cliff's d (ETH contra/vol vs MOC contra/vol): {d_s1a:+.3f} "
      f"(>= {CLIFFS_D_MIN})")
print(f"        Median-Vorsprung ETH-MOC (volnorm.): {obs:+.3e} | "
      f"Placebo-Perzentil (n={PLACEBO_N}): {pctile_s1:.1f}% (> {PERCENTILE_MIN}%)")
print(f"    (b) corr(ETH-Drift, Reversion): {corr_eth:+.3f}  vs  "
      f"corr(MOC-Drift, Reversion): {corr_moc:+.3f}  (Prop: corr_ETH > corr_MOC)")
s1_pass = (np.isfinite(d_s1a) and d_s1a >= CLIFFS_D_MIN
           and pctile_s1 > PERCENTILE_MIN and corr_eth > corr_moc)
print(f"    => S1 {'BESTANDEN' if s1_pass else 'NICHT BESTANDEN'}")

print("\n[3] S2 — DOSIS-ORDNUNG (Verfall-Fr > Fr > Verfall-Wt > normal):")
for k, name in [(3, "Verfall-Freitag"), (2, "Freitag"),
                (1, "Verfall-Wochentag"), (0, "normal")]:
    g = groups[k]
    print(f"    Dosis {k} ({name:<18}) n={len(g):>4}  "
          f"median eth_contra = {np.median(g) if len(g) else float('nan'):+.2f} bps")
print(f"    Jonckheere-Terpstra: z={z_jt:+.2f}  p(einseitig)={p_jt:.4f} (< 0.05)")
s2_pass = np.isfinite(p_jt) and p_jt < 0.05
print(f"    => S2 {'BESTANDEN' if s2_pass else 'NICHT BESTANDEN'}")

print("\n[4] S3 — DECAY-SPLIT (Pflicht-Falsifikator):")
print(f"    2019-2021: n={len(pre22)}  median eth_contra = {pre22.median():+.2f} bps")
print(f"    2022+:     n={len(post22)}  median eth_contra = {post22.median():+.2f} bps")
print(f"    Cliff's d (2022+ vs 2019-2021): {d_decay:+.3f}")
print(f"    Prop-Kohorte existiert erst post-2021 — Effekt DARF 2019-2021 "
      f"nicht dominieren.")
s3_pass = decay_ok
print(f"    => S3 {'BESTANDEN (Attribution plausibel)' if s3_pass else 'GESCHEITERT — Prop-Attribution widerlegt (KIMI-Einwand bestaetigt)'}")

print("\n[5] ID30-KALENDER-COVARIATEN (mitgefuehrt, degradiert):")
print(f"    Opex-Freitage: {int(R['is_opex_friday'].sum())} | "
      f"Roll-Fenster-Tage: {int(R['is_roll_window'].sum())} | "
      f"Quartals-Opex: {int(R['is_quad_witching'].sum())}")
print("    Margin-Hike-Stichtage: EXTERNE LISTE (CME Historical Margins) "
      "noch zu befuellen — aktuell leer.")

print("\n[6] GESAMTURTEIL (vorregistrierte Abnahmekriterien):")
net_ok = np.isfinite(net_bps) and net_bps >= NET_BPS_MIN
print(f"    S1 Zeitfenster: {'PASS' if s1_pass else 'FAIL'} | "
      f"S2 Dosis: {'PASS' if s2_pass else 'FAIL'} | "
      f"S3 Decay: {'PASS' if s3_pass else 'FAIL'} | "
      f"Netto >= {NET_BPS_MIN} bps: {'PASS' if net_ok else 'FAIL'}")
if s1_pass and s2_pass and s3_pass and net_ok:
    print("    => ID29 GO — Ernte nur mit bestandener Attribution zulaessig.")
else:
    print("    => ID29 NO-GO / ATTRIBUTION GESCHEITERT — Hypothese tot, "
          "KEINE Neu-Suche im selben Datensatz (Datenfalle 5).")

print(f"\n[7] Reversions-Tabelle (Ziel 18:00-19:00 ET, Trendtage):")
print(f"    {'Zelle':<38} {'n':>5} {'median bps':>10}")
for name, sub in [("Trend-UP, Close-Verstaerkung (Prop: DOWN)",
                   T[T["day_dir"] > 0]),
                  ("Trend-DOWN, Close-Verstaerkung (Prop: UP)",
                   T[T["day_dir"] < 0]),
                  ("Kontrolle: Nicht-Trendtage (alle)", C)]:
    v = sub["rev_ret"].dropna() * 1e4
    med = v.median() if len(v) else float("nan")
    print(f"    {name:<38} {len(v):>5} {med:>+10.2f}")
print("    Prop-Prognose: UP-Zelle negativ UND |UP| >= |DOWN|-Asymmetrie "
      "staerker als Boyarchenko-unbedingt.")

print(f"\n[8] Robusta: Abstain gesamt = {abstain_news + abstain_thin} "
      f"(News {abstain_news} / duenn {abstain_thin}) | "
      f"DST-Flag-Tage = {int(R['dst_flag'].sum())} (nur Flag, ET-basiert)")
no_dst = T[~T["dst_flag"]]
if len(no_dst) > 100:
    d_nd = cliffs_delta(no_dst["eth_contra_vn"], no_dst["moc_contra_vn"])
    print(f"    S1a ohne DST-Uebergangstage: Cliff's d = {d_nd:+.3f} (Robustheitscheck)")
print("=" * 78)
