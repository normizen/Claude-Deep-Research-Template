# Feasibility: ID52k — Cross-Instrument-Bet-Hedging

**Datum:** 2026-09-05 | **Runde:** 3 | **Status:** Feasibility-Urteil

**Idee (1 Satz):** Dasselbe tägliche 0DTE-Gamma-Zwang-Ende (16:00 ET) in vier Instrumenten (ES, NQ, GC, ZB) — Entry gegen den jeweiligen Close-Flow, Erfolgsmaß = geometrisches Mittel über die 4 × 250 = 1000 Replikate/Jahr, stratifiziert nach Instrumenten-Regime, Varianz zwischen Instrumenten als Fitnessträger.

---

## Gate 1: Brutto-Wirtssignal mechanisch plausibel? — ✅ ERFÜLLT

- **Zwang:** Tägliches 0DTE-Options-Gamma-Ende 16:00 ET; Richtung durch den Zwang diktiert (Entry GEGEN den jeweiligen Close-Flow), Zeitpunkt kalenderfest.
- **Einschränkung (aus pre-KIMI/pre-OPUS):** Das scharfe 16:00-ET-Gamma-Ende ist für ES/NQ sauber begründet; für GC/ZB (COMEX/CBOT-Settlement-Zeiten weichen ab) ist die Homogenität des Zwangs eine **Annahme, kein Befund**. Wenn GC/ZB nicht mitziehen, sinkt die effektive Replikatzahl von 4 auf 2 pro Tag.
- Mechanistische Plausibilität des Kern-Trades (0DTE-Reversion am Zwang-Ende, A19/A23/A19) ist gegeben; Gate erfüllt mit dokumentiertem GC/ZB-Vorbehalt.

## Gate 2: QC-Messbarkeit 1–2 h/Tag? — ✅ ERFÜLLT

- Minutenbars ES/NQ/GC/ZB auf QuantConnect, tägliche Ereignisstudie, geometrisches Mittel über 4 Replikate, vorregistrierte Regime-Labels. Beide Advocatus-Gutachten bestätigen: 1 h/Tag ✓, kein neuer Daten-Feed > 50 $.

## Gate 3: Einpreisung? — ⚠️ TEILWEISE

- „Buy the close reversal" ist retail-bekannt; die Panel-Kodierung über 4 Instrumente mit Placebo-Zufallsuhrzeiten ist nicht das eingepreiste Einzelmarkt-Momentum (pre-KIMI zu 41o).
- Substitutionsresistenz des **Bet-Hedging-Formalismus** selbst ist hoch (pre-OPUS: institutionelle Cross-Asset-Strategien nutzen Cointegration/PCA, nicht Bet-Hedging-Replikate).
- Aber: Einpreisungs-Risiko sitzt im **Trade**, nicht in der **Metrik** — und der Trade ist identisch mit ID41o.

## Gate 4: Überschneidung mit ID41o — Eigenständigkeit? — ❌ NICHT EIGENSTÄNDIG

Entscheidender Befund aus pre-KIMI (Advocatus):

> „52k ≈ 41o mit Bet-Hedging-Metrik statt Panel-Event-Study — **derselbe Trade, gleiche Fenster**."

- **Trade-Identität:** Entry 16:00 ET gegen den Close-Flow, 4 Instrumente, täglich — identisch zu ID41o. ID52k führt **keinen neuen Zwang, kein neues Fenster, keine neue Richtung** ein.
- **Metrik-Differenz:** Das geometrische Mittel über Replikate ist kein Markt-Signal, sondern ein Auswertungs-Layer auf ID41o-Daten. Genau derselbe Formalismus existiert bereits als ID44k (Bet-Hedging-Replikat-Statistik) — ID52k ist damit zusammengesetzt aus ID41o (Trade) + ID44k (Metrik), ohne eigenen additiven Mechanismus.
- **Präzedenz im Advocatus:** ID47o und ID51o wurden mit identischer Begründung getötet („Auswertungs-/Sizing-Layer auf 41o-Daten ohne eigenen Zwang — gehört ins 41o-Protokoll, nicht ins Ideen-Register"). Konsistenz gebietet dasselbe Urteil für ID52k.
- **Offene Abhängigkeit:** A25s Unabhängigkeitsannahme (4 quasi-unabhängige Replikate) ist ungeprüft (ID53o testet sie); ohne 53o droht Klumpen-Überzählung, und das „geometrische Mittel über 1000 Replikate" erzeugt falsche Power-Sicherheit. Das betrifft 41o und 52k gleichermaßen — kein Differenzierungsmerkmal.

---

## Urteil

**MODUL-VON-ID41o**

ID52k hat ein mechanisch plausibles Wirtsignal und ist in 1 h/Tag QC-messbar, bringt aber weder einen neuen Zwang noch ein neues Fenster — der Trade ist deckungsgleich mit ID41o. Sein einziger Beitrag ist der Bet-Hedging-Formalismus (geometrisches Mittel, Regime-Stratifizierung), und der ist bereits als ID44k im Register bzw. als Metrik-Aufsatz klassifiziert, nicht als eigenständige Markt-Hypothese. Der Bet-Hedging-Formalismus ist als Auswertungs-Abschnitt (Erfolgsmaß: geometrisches Mittel über die 4 Instrumenten-Replikate, stratifiziert nach Regime) in das ID41o-Protokoll zu übernehmen — als eigenständige Idee erfüllt ID52k das Eigenständigkeits-Gate nicht.
