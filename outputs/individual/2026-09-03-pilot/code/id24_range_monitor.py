#!/usr/bin/env python3
"""id24_range_monitor.py — Instrumenten-Apoptose: 20-Tage-Dollar-Ranges + Kosten/Range-Ratios.

Teil von ID24 (6-Kriterien-Eliminierungsturnier). Berechnet Kriterium K1
(Kosten-Range-Schere: All-in-RT-Kosten > 5 % der 20-Tage-Durchschnittsrange)
fuer ES, NQ, MES, MNQ aus Daily-Bars (CSV-Export aus QuantConnect).

Erwartetes CSV-Format (eine Datei pro Instrument ODER eine kombinierte Datei):
    date,open,high,low,close[,symbol]
    2026-08-03,6450.25,6478.50,6432.00,6470.00[,ES]

Verwendung:
    # Kombinierte Datei mit symbol-Spalte:
    python id24_range_monitor.py --csv daily_bars.csv --rt-costs ES=13.0 MES=4.5 NQ=14.0 MNQ=4.5

    # Separate Dateien pro Instrument:
    python id24_range_monitor.py --csv-dir ./bars/ --rt-costs ES=13.0 MES=4.5 NQ=14.0 MNQ=4.5

    # Kapital fuer K2/K3-Kontextausgabe:
    python id24_range_monitor.py --csv daily_bars.csv --rt-costs ES=13.0 --capital 7500

Multiplikatoren (CME-Spezifikation, stabil — Datenfalle: nicht raten, fix dokumentiert):
    ES  = 50 USD/Punkt   (Tick 0.25 = 12.50 USD)
    MES = 5 USD/Punkt    (Tick 0.25 = 1.25 USD)
    NQ  = 20 USD/Punkt   (Tick 0.25 = 5.00 USD)
    MNQ = 2 USD/Punkt    (Tick 0.25 = 0.50 USD)

Ausgabe: Tabelle mit 20-Tage-Range in USD, Kosten/Range-Ratio, K1-Status.
Exit-Code 1 wenn mindestens ein Instrument K1 verletzt (tot).
"""
import argparse
import csv
import sys
from collections import defaultdict

MULTIPLIERS = {"ES": 50.0, "MES": 5.0, "NQ": 20.0, "MNQ": 2.0}
K1_THRESHOLD = 0.05  # 5 % der 20-Tage-Range (vorab registrierter Schwellwert)


def load_bars(path, symbol_filter=None):
    bars = defaultdict(list)  # symbol -> list[(date, high, low)]
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        cols = {c.lower() for c in (reader.fieldnames or [])}
        if not {"date", "high", "low"} <= cols:
            sys.exit(f"FEHLER: {path} braucht Spalten date,high,low (gefunden: {reader.fieldnames})")
        for row in reader:
            sym = row.get("symbol") or row.get("Symbol") or symbol_filter
            if sym is None:
                sys.exit("FEHLER: CSV hat keine symbol-Spalte; --symbol angeben oder symbol-Spalte ergaenzen.")
            sym = sym.upper()
            if symbol_filter and sym != symbol_filter.upper():
                continue
            bars[sym].append((row["date"], float(row["high"]), float(row["low"])))
    return bars


def dollar_range_20d(bars, mult):
    """20-Tage-Durchschnittsrange in USD (letzte 20 Eintraege, chronologisch sortiert)."""
    bars = sorted(bars, key=lambda b: b[0])[-20:]
    if len(bars) < 20:
        return None, len(bars)
    avg_pts = sum(h - l for _, h, l in bars) / len(bars)
    return avg_pts * mult, len(bars)


def main():
    ap = argparse.ArgumentParser(description="ID24 Range-Monitor (K1: Kosten/Range-Schere)")
    ap.add_argument("--csv", help="Eine CSV-Datei (mit symbol-Spalte oder --symbol)")
    ap.add_argument("--csv-dir", help="Verzeichnis mit <SYMBOL>.csv Dateien")
    ap.add_argument("--symbol", help="Symbol erzwingen, wenn CSV ohne symbol-Spalte")
    ap.add_argument("--rt-costs", nargs="+", required=True,
                    help="All-in-RT-Kosten pro Instrument, z.B. ES=13.0 MES=4.5")
    ap.add_argument("--capital", type=float, default=None, help="Kontokapital fuer Kontext (optional)")
    args = ap.parse_args()

    if not args.csv and not args.csv_dir:
        ap.error("--csv oder --csv-dir erforderlich")

    rt_costs = {}
    for kv in args.rt_costs:
        sym, val = kv.split("=")
        rt_costs[sym.upper()] = float(val)

    # Daten laden
    bars_by_sym = defaultdict(list)
    if args.csv:
        for sym, bars in load_bars(args.csv, args.symbol).items():
            bars_by_sym[sym].extend(bars)
    else:
        import os, glob
        for path in sorted(glob.glob(os.path.join(args.csv_dir, "*.csv"))):
            sym = os.path.splitext(os.path.basename(path))[0].upper()
            bars_by_sym[sym].extend(load_bars(path, sym)[sym])

    print(f"{'Sym':<5} {'n':>3} {'Range20d ($)':>13} {'RT-Kosten ($)':>14} {'Kosten/Range':>13}  K1 (Schwelle 5%)")
    print("-" * 75)
    any_dead = False
    for sym in ("ES", "MES", "NQ", "MNQ"):
        if sym not in bars_by_sym:
            continue
        rng, n = dollar_range_20d(bars_by_sym[sym], MULTIPLIERS[sym])
        cost = rt_costs.get(sym)
        if rng is None:
            print(f"{sym:<5} {n:>3} {'zu wenig Daten (<20 Tage)':>13}")
            continue
        if cost is None:
            print(f"{sym:<5} {n:>3} {rng:>13,.2f} {'--fehlt--':>14}")
            continue
        ratio = cost / rng
        status = "TOT (sofort)" if ratio > K1_THRESHOLD else "ok"
        if ratio > K1_THRESHOLD:
            any_dead = True
        print(f"{sym:<5} {n:>3} {rng:>13,.2f} {cost:>14,.2f} {ratio:>12.1%}  {status}")

    if args.capital:
        print(f"\nKontext (Kapital {args.capital:,.0f}): K1-Schwelle entspricht RT-Kosten > "
              f"{K1_THRESHOLD:.0%} der Range. K2/K3 aus CME-Margin-Bulletin separat pruefen.")
    sys.exit(1 if any_dead else 0)


if __name__ == "__main__":
    main()
