# ============================================================================
# ID24 — K1: Kosten/Range-Schere  (ES, NQ, MES, MNQ)
# ============================================================================
# Eine einzige, vollstaendig lauffaehige Zelle fuer das QC-Research-Notebook
# (QuantBook-Umgebung, Variable `qb` vorhanden). In eine neue Zelle kopieren
# und ausfuehren.
#
# ----------------------------------------------------------------------------
# KRITERIUM K1 (aus ID24, 6-Kriterien-Eliminierungsturnier):
#   Ein Instrument ist "tot", wenn die All-in-Round-Trip-Kosten groesser sind
#   als K1_THRESHOLD (5 %) der 20-Handelstage-Durchschnittsrange in USD.
#
# RANGE-DEFINITION: mittlere Tages-Range = mean(high - low) ueber die letzten
#   20 Handelstage, in Indexpunkten, mal CME-Multiplikator = USD.
#
# MICROS: MES/MNQ tracken denselben Index wie ES/NQ -> identische Punkt-Range,
#   nur der Multiplikator unterscheidet sich. Daher wird nur ES + NQ von QC
#   geladen und MES/MNQ daraus abgeleitet.
#
# DATENFALLE (dokumentiert): continuous future,
#   data_mapping_mode = OPEN_INTEREST,
#   data_normalization_mode = BACKWARDS_RATIO (backadjusted).
#   QC-API-Namen seit PEP8-Umstellung: SCREAMING_SNAKE, teils gekuerzt.
# ============================================================================

from datetime import datetime, timedelta

# ------------------------- KONFIGURATION -----------------------------------
LOOKBACK_TRADING_DAYS = 20        # K1 misst die 20-Handelstage-Durchschnittsrange
HISTORY_CALENDAR_DAYS = 90        # Rueckschau-Puffer (Wochenenden/Feiertage)
K1_THRESHOLD          = 0.05      # RT-Kosten > 5 % der Range  -> Instrument tot

# All-in Round-Trip-Kosten in USD (Kommission + Gebuehren + 1 Tick Slippage)
RT_COSTS = {"ES": 13.0, "MES": 4.5, "NQ": 14.0, "MNQ": 4.5}

# CME-Multiplikatoren (USD pro Indexpunkt) — fix dokumentiert, nicht raten
MULT = {"ES": 50.0, "MES": 5.0, "NQ": 20.0, "MNQ": 2.0}

# Welche QC-Serie liefert die Punkt-Range fuer welche Symbole
SERIES = [
    (Futures.Indices.SP_500_E_MINI,     ["ES",  "MES"]),
    (Futures.Indices.NASDAQ_100_E_MINI, ["NQ",  "MNQ"]),
]

END   = datetime.now()
START = END - timedelta(days=HISTORY_CALENDAR_DAYS)

# ------------------------- DATEN + 20-TAGE-RANGE JE SERIE ------------------
range_pts_by_sym = {}   # symbol -> (avg_range_in_points, n_bars)

for qc_const, syms in SERIES:
    future = qb.add_future(
        qc_const,
        Resolution.DAILY,
        data_mapping_mode=DataMappingMode.OPEN_INTEREST,
        data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO,
        contract_depth_offset=0,
    )
    hist = qb.history(future.symbol, START, END, Resolution.DAILY)

    if hist is None or len(hist) == 0:
        for s in syms:
            range_pts_by_sym[s] = (None, 0)
        print(f"WARNUNG: keine History fuer {syms[0]} ({qc_const}) — "
              f"HISTORY_CALENDAR_DAYS erhoehen?")
        continue

    # letzte N Handelstage; Range je Tag = high - low (in Punkten)
    tail = hist.tail(LOOKBACK_TRADING_DAYS)
    n = len(tail)
    avg_range_pts = float((tail["high"] - tail["low"]).mean())
    for s in syms:
        range_pts_by_sym[s] = (avg_range_pts, n)

# ------------------------- K1-TABELLE -------------------------------------
print("\n" + "=" * 78)
print(f"ID24 — K1: Kosten/Range-Schere   (Range = {LOOKBACK_TRADING_DAYS} Handelstage, "
      f"Schwelle {K1_THRESHOLD:.0%})")
print(f"Zeitraum: {START:%Y-%m-%d} .. {END:%Y-%m-%d}   |   continuous, "
      f"OPEN_INTEREST / BACKWARDS_RATIO")
print("=" * 78)
print(f"{'Sym':<5} {'n':>3} {'Range20d ($)':>14} {'RT-Kosten ($)':>14} "
      f"{'Kosten/Range':>13}  K1")
print("-" * 78)

any_dead = False
for sym in ("ES", "MES", "NQ", "MNQ"):
    avg_pts, n = range_pts_by_sym.get(sym, (None, 0))
    if avg_pts is None or n < LOOKBACK_TRADING_DAYS:
        print(f"{sym:<5} {n:>3}   zu wenig Daten (<{LOOKBACK_TRADING_DAYS} Handelstage)")
        continue
    range_usd = avg_pts * MULT[sym]
    cost = RT_COSTS.get(sym)
    if cost is None:
        print(f"{sym:<5} {n:>3} {range_usd:>14,.2f} {'--Kosten fehlt--':>14}")
        continue
    ratio = cost / range_usd
    dead = ratio > K1_THRESHOLD
    any_dead = any_dead or dead
    print(f"{sym:<5} {n:>3} {range_usd:>14,.2f} {cost:>14,.2f} "
          f"{ratio:>12.1%}  {'TOT (sofort)' if dead else 'ok'}")

print("-" * 78)
print("K1-ERGEBNIS:", "MINDESTENS EIN INSTRUMENT TOT" if any_dead else "alle ok")
print("=" * 78)
