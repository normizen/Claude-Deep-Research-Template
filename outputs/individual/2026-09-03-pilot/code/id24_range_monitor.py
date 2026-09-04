#!/usr/bin/env python3
"""id24_range_monitor.py — Instrumenten-Apoptose: 20-Tage-Dollar-Ranges + Kosten/Range-Ratios.

Teil von ID24 (6-Kriterien-Eliminierungsturnier). Berechnet Kriterium K1
(Kosten-Range-Schere: All-in-RT-Kosten > 5 % der 20-Tage-Durchschnittsrange)
fuer ES, NQ, MES, MNQ aus Daily-Bars.

Laeuft in ZWEI Modi:

  A) Als CLI-Script (Terminal):
       python id24_range_monitor.py --csv daily_bars.csv --rt-costs ES=13.0 MES=4.5 NQ=14.0 MNQ=4.5
       python id24_range_monitor.py --csv-dir ./bars/  --rt-costs ES=13.0 MES=4.5
       python id24_range_monitor.py --csv daily_bars.csv --rt-costs ES=13.0 --capital 7500

  B) Im QuantConnect-Research-Notebook (einfachster Weg):
           %run id24_range_monitor.py
           run_qc(qb)                 # holt ES/NQ/MES/MNQ selbst via qb.history
       Optional: run_qc(qb, rt_costs={...}, days=60, capital=7500)

  C) Im Jupyter-/QuantConnect-Notebook mit eigenem DataFrame:
           run(bars_df=my_dataframe, rt_costs={"ES": 13.0, "MES": 4.5})
       oder oben im Block "NOTEBOOK-KONFIG" die Werte setzen und die
       if __name__ == "__main__"-Zelle ausfuehren. argparse wird im Notebook
       NICHT benutzt (dort ist sys.argv der Kernel-Launcher).

Erwartetes CSV-Format (eine Datei pro Instrument ODER eine kombinierte Datei):
    date,open,high,low,close[,symbol]
    2026-08-03,6450.25,6478.50,6432.00,6470.00[,ES]

Erwartetes DataFrame-Format (Notebook): Spalten date, high, low und entweder eine
symbol-Spalte oder symbol= an run() uebergeben. QuantConnect-History:
    hist = qb.history(qb.add_equity(...).symbol, 30, Resolution.DAILY)
    df = hist.reset_index()[["time", "high", "low"]].rename(columns={"time": "date"})
    df["symbol"] = "ES"

Multiplikatoren (CME-Spezifikation, stabil — Datenfalle: nicht raten, fix dokumentiert):
    ES  = 50 USD/Punkt   (Tick 0.25 = 12.50 USD)
    MES = 5 USD/Punkt    (Tick 0.25 = 1.25 USD)
    NQ  = 20 USD/Punkt   (Tick 0.25 = 5.00 USD)
    MNQ = 2 USD/Punkt    (Tick 0.25 = 0.50 USD)

Ausgabe: Tabelle mit 20-Tage-Range in USD, Kosten/Range-Ratio, K1-Status.
Rueckgabe von run(): True wenn mindestens ein Instrument K1 verletzt (tot).
CLI-Exit-Code: 1 wenn tot, sonst 0.
"""
import argparse
import csv
import sys
from collections import defaultdict

MULTIPLIERS = {"ES": 50.0, "MES": 5.0, "NQ": 20.0, "MNQ": 2.0}
K1_THRESHOLD = 0.05  # 5 % der 20-Tage-Range (vorab registrierter Schwellwert)

# ============================================================================
# NOTEBOOK-KONFIG — nur relevant wenn die Datei im Notebook ausgefuehrt wird.
# Im Terminal werden diese Werte ignoriert (dort zaehlen die --flags).
# ----------------------------------------------------------------------------
CSV      = None          # z.B. "daily_bars.csv"  (kombinierte Datei)
CSV_DIR  = None          # z.B. "./bars/"         (eine <SYMBOL>.csv je Instrument)
SYMBOL   = None          # erzwingen, wenn CSV/DF keine symbol-Spalte hat
BARS_DF  = None          # pandas.DataFrame mit Spalten date, high, low [, symbol]
RT_COSTS = {             # All-in-Round-Trip-Kosten pro Instrument in USD
    "ES":  13.0,
    "MES":  4.5,
    "NQ":  14.0,
    "MNQ":  4.5,
}
CAPITAL  = None          # z.B. 7500.0 fuer die K2/K3-Kontextzeile
# ============================================================================


class ConfigError(Exception):
    """Fehlende/ungueltige Eingabe — im Notebook als normale Exception sichtbar."""


def _in_notebook():
    """True, wenn wir in einem IPython-Kernel (Jupyter/QC) laufen, nicht im Terminal."""
    try:
        from IPython import get_ipython
        ip = get_ipython()
        return ip is not None and ip.__class__.__name__ == "ZMQInteractiveShell"
    except Exception:
        return False


def load_bars(path, symbol_filter=None):
    bars = defaultdict(list)  # symbol -> list[(date, high, low)]
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        cols = {c.lower() for c in (reader.fieldnames or [])}
        if not {"date", "high", "low"} <= cols:
            raise ConfigError(
                f"{path} braucht Spalten date,high,low (gefunden: {reader.fieldnames})")
        for row in reader:
            sym = row.get("symbol") or row.get("Symbol") or symbol_filter
            if sym is None:
                raise ConfigError(
                    "CSV hat keine symbol-Spalte; --symbol / SYMBOL angeben oder Spalte ergaenzen.")
            sym = sym.upper()
            if symbol_filter and sym != symbol_filter.upper():
                continue
            bars[sym].append((row["date"], float(row["high"]), float(row["low"])))
    return bars


def load_bars_df(df, symbol_filter=None):
    """Bars aus einem pandas.DataFrame (Spalten date, high, low [, symbol])."""
    bars = defaultdict(list)
    cols = {c.lower(): c for c in df.columns}
    if not {"date", "high", "low"} <= set(cols):
        raise ConfigError(
            f"DataFrame braucht Spalten date,high,low (gefunden: {list(df.columns)})")
    sym_col = cols.get("symbol")
    for _, row in df.iterrows():
        sym = (str(row[sym_col]) if sym_col else None) or symbol_filter
        if sym is None:
            raise ConfigError(
                "DataFrame hat keine symbol-Spalte; symbol= an run() uebergeben oder Spalte ergaenzen.")
        sym = sym.upper()
        if symbol_filter and sym != symbol_filter.upper():
            continue
        bars[sym].append((str(row[cols["date"]]), float(row[cols["high"]]), float(row[cols["low"]])))
    return bars


def dollar_range_20d(bars, mult):
    """20-Tage-Durchschnittsrange in USD (letzte 20 Eintraege, chronologisch sortiert)."""
    bars = sorted(bars, key=lambda b: b[0])[-20:]
    if len(bars) < 20:
        return None, len(bars)
    avg_pts = sum(h - l for _, h, l in bars) / len(bars)
    return avg_pts * mult, len(bars)


def run(csv=None, csv_dir=None, symbol=None, bars_df=None, rt_costs=None, capital=None):
    """Kernlogik. Gibt True zurueck, wenn mindestens ein Instrument K1 verletzt.

    Genau EINE Datenquelle angeben: csv ODER csv_dir ODER bars_df.
    rt_costs: dict {SYMBOL: USD} oder Liste ["ES=13.0", ...].
    """
    sources = [x for x in (csv, csv_dir, bars_df is not None and "df") if x]
    if not sources:
        raise ConfigError("Keine Datenquelle: csv, csv_dir oder bars_df angeben.")
    if len(sources) > 1:
        raise ConfigError("Nur EINE Datenquelle angeben (csv / csv_dir / bars_df).")

    # rt_costs normalisieren
    if rt_costs is None:
        raise ConfigError("rt_costs fehlt (z.B. {'ES': 13.0} oder ['ES=13.0']).")
    if isinstance(rt_costs, dict):
        rt = {k.upper(): float(v) for k, v in rt_costs.items()}
    else:
        rt = {}
        for kv in rt_costs:
            k, v = kv.split("=")
            rt[k.upper()] = float(v)

    # Daten laden
    bars_by_sym = defaultdict(list)
    if bars_df is not None:
        for sym, bars in load_bars_df(bars_df, symbol).items():
            bars_by_sym[sym].extend(bars)
    elif csv:
        for sym, bars in load_bars(csv, symbol).items():
            bars_by_sym[sym].extend(bars)
    else:
        import os
        import glob
        paths = sorted(glob.glob(os.path.join(csv_dir, "*.csv")))
        if not paths:
            raise ConfigError(f"Keine *.csv in {csv_dir!r} gefunden.")
        for path in paths:
            sym = os.path.splitext(os.path.basename(path))[0].upper()
            bars_by_sym[sym].extend(load_bars(path, sym)[sym])

    print(f"{'Sym':<5} {'n':>3} {'Range20d ($)':>13} {'RT-Kosten ($)':>14} {'Kosten/Range':>13}  K1 (Schwelle 5%)")
    print("-" * 75)
    any_dead = False
    for sym in ("ES", "MES", "NQ", "MNQ"):
        if sym not in bars_by_sym:
            continue
        rng, n = dollar_range_20d(bars_by_sym[sym], MULTIPLIERS[sym])
        cost = rt.get(sym)
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

    if capital:
        print(f"\nKontext (Kapital {capital:,.0f}): K1-Schwelle entspricht RT-Kosten > "
              f"{K1_THRESHOLD:.0%} der Range. K2/K3 aus CME-Margin-Bulletin separat pruefen.")
    return any_dead


def run_qc(qb, rt_costs=None, days=45, capital=None):
    """Bequem-Wrapper fuer das QuantConnect-Research-Notebook.

    Holt Daily-Bars fuer ES + NQ direkt via qb.history, leitet MES/MNQ daraus ab
    (Micros tracken denselben Index -> identische Punkt-Range) und wertet K1 aus.

        %run id24_range_monitor.py
        run_qc(qb)

    qb        : QuantBook-Instanz aus dem Notebook
    rt_costs  : dict {SYMBOL: USD}; Default = grobe All-in-Schaetzung
    days      : Kalendertage Rueckschau (Puffer, es braucht >= 20 Handelstage)
    capital   : optionale Kontext-Zeile
    """
    from datetime import timedelta
    try:
        import pandas as pd  # im QC-Research-Kernel vorhanden
        import importlib
        qc = importlib.import_module("AlgorithmImports")
        Futures = qc.Futures
        Resolution = qc.Resolution
        DataMappingMode = qc.DataMappingMode
        DataNormalizationMode = qc.DataNormalizationMode
    except Exception as e:  # pragma: no cover - nur ausserhalb QC
        raise ConfigError(
            f"run_qc() braucht die QuantConnect-Research-Umgebung ({e}). "
            "Ausserhalb QC: run(bars_df=...) mit eigenem DataFrame benutzen.") from e

    if rt_costs is None:
        rt_costs = {"ES": 13.0, "MES": 4.5, "NQ": 14.0, "MNQ": 4.5}

    specs = [
        (Futures.Indices.SP_500_E_MINI,     "ES",  "MES"),
        (Futures.Indices.NASDAQ_100_E_MINI, "NQ",  "MNQ"),
    ]
    frames = []
    for const, mini, micro in specs:
        fut = qb.add_future(
            const, Resolution.DAILY,
            data_mapping_mode=DataMappingMode.OPEN_INTEREST,
            data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO,
            contract_depth_offset=0,
        )
        hist = qb.history(fut.symbol, timedelta(days=days), Resolution.DAILY)
        if hist is None or len(hist) == 0:
            raise ConfigError(f"Keine History fuer {mini} ({const}) — days erhoehen?")
        h = hist.reset_index()
        tcol = "time" if "time" in h.columns else next(
            (c for c in h.columns if "time" in str(c).lower()), h.columns[0])
        h = h[[tcol, "high", "low"]].rename(columns={tcol: "date"})
        frames.append(h.assign(symbol=mini))
        frames.append(h.assign(symbol=micro))

    bars = pd.concat(frames, ignore_index=True)
    print(f"run_qc: {len(bars)} Bars ({', '.join(sorted(bars['symbol'].unique()))}), "
          f"Zeitraum {bars['date'].min()} .. {bars['date'].max()}\n")
    return run(bars_df=bars, rt_costs=rt_costs, capital=capital)


def main(argv=None):
    ap = argparse.ArgumentParser(description="ID24 Range-Monitor (K1: Kosten/Range-Schere)")
    ap.add_argument("--csv", help="Eine CSV-Datei (mit symbol-Spalte oder --symbol)")
    ap.add_argument("--csv-dir", help="Verzeichnis mit <SYMBOL>.csv Dateien")
    ap.add_argument("--symbol", help="Symbol erzwingen, wenn CSV ohne symbol-Spalte")
    ap.add_argument("--rt-costs", nargs="+", required=True,
                    help="All-in-RT-Kosten pro Instrument, z.B. ES=13.0 MES=4.5")
    ap.add_argument("--capital", type=float, default=None, help="Kontokapital fuer Kontext (optional)")
    args = ap.parse_args(argv)

    if not args.csv and not args.csv_dir:
        ap.error("--csv oder --csv-dir erforderlich")

    try:
        any_dead = run(csv=args.csv, csv_dir=args.csv_dir, symbol=args.symbol,
                       rt_costs=args.rt_costs, capital=args.capital)
    except ConfigError as e:
        sys.exit(f"FEHLER: {e}")
    sys.exit(1 if any_dead else 0)


if __name__ == "__main__":
    if _in_notebook():
        # Notebook: argparse ueberspringen. Nur rechnen, wenn oben im
        # NOTEBOOK-KONFIG-Block etwas gesetzt wurde — sonst nur ein Hinweis,
        # damit das blosse Laden der Datei nicht mit einem Fehler abbricht.
        if CSV or CSV_DIR or BARS_DF is not None:
            _dead = run(csv=CSV, csv_dir=CSV_DIR, symbol=SYMBOL, bars_df=BARS_DF,
                        rt_costs=RT_COSTS, capital=CAPITAL)
            print(f"\nK1-Ergebnis: {'MINDESTENS EIN INSTRUMENT TOT' if _dead else 'alle ok'}")
        else:
            print(
                "id24_range_monitor geladen — noch keine Daten konfiguriert.\n"
                "Naechster Schritt in einer NEUEN Zelle:\n"
                "    run_qc(qb)                                  # QC holt ES/NQ/MES/MNQ selbst\n"
                "  oder\n"
                "    run(bars_df=DEIN_DF, rt_costs={'ES': 13.0, 'MES': 4.5, 'NQ': 14.0, 'MNQ': 4.5})\n"
                "  oder oben im NOTEBOOK-KONFIG-Block CSV / CSV_DIR / BARS_DF setzen."
            )
    else:
        main()
