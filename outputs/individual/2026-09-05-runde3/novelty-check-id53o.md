# Novelty Check ID53o — Flip-Kohärenz-Test (Cross-Instrument-Reversion als Panel-Validierung)

## Idee
Empirische Prüfung der A25-Unabhängigkeitsannahme: Flippen Reversions-Richtungen zwischen den 4 Instrumenten (ES/NQ/GC/ZB) kohärent (gleiches Vorzeichen am selben Tag) oder unabhängig? Misst, ob das Cross-Instrument-Panel echte Replikate liefert oder nur 4× denselben Trade.

## Suche
Publizierte Tests der Cross-Asset-Kohärenz von Intraday-Reversion (ES/NQ/GC/ZB) als Validierung von Panel-Replikaten?

## Befunde
- **Cross-Asset-Korrelationsmatrizen** für ES/NQ/ZB/GC existieren (CrossVol, ClearEdge, NexusFi Intermarket Guides) — aber auf Return-Ebene, nicht auf Signal-/Flip-Ebene, und nicht als Unabhängigkeits-Validierung eines Reversions-Panels.
- **Intraday-Reversion-Literatur**: Liu et al. 2025 ("Overnight-Intraday Reversal Everywhere", Cross-Asset-Reversion, aber als Anomalie-Dokumentation, nicht als Kohärenz-Test der Signale); Chu & Song 2023 (China, einzelner Markt); chinesische Commodity-Futures-Reversal-Studien. Keine misst die tagesgleiche Vorzeichen-Kohärenz des Reversions-Trades über ein kleines Futures-Panel.
- **RORO/Common-Factor-Literatur** (Risk-On/Risk-Off) dokumentiert gemeinsame Return-Faktoren, wird aber nicht als Test der Replikate-Annahme in Panel-Backtests formuliert.
- **Effektive-Stichprobengröße / Clustering in Panel-Backtests** (z. B. Newey-West, Cluster-SE) existiert methodisch, aber kein publizierter "Flip-Kohärenz-Test" als konkrete Diagnostik für ein 4-Instrumenten-Reversions-Panel.

## Urteil
NOVEL

Der spezifische Test — tagesgleiche Vorzeichen-Kohärenz der Reversions-Flips über ES/NQ/GC/ZB als Diagnostik, ob das Panel echte unabhängige Replikate oder denselben Trade 4× liefert — ist in der Literatur nicht publiziert; existierende Arbeiten decken Return-Korrelationen oder Einzelmarkt-Reversion ab, nicht die Signal-Kohärenz als Panel-Validierung.
