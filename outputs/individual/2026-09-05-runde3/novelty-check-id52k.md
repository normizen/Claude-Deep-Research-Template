# Novelty-Check ID52k — Cross-Instrument-Bet-Hedging (0DTE-Ende × ES/NQ/GC/ZB)

**Kernmechanik:** Dasselbe tägliche 0DTE-Gamma-Ende wird in vier Instrumenten (ES, NQ, GC, ZB) als vier Realisierungen desselben Zwangs behandelt; Erfolgsmaß ist das geometrische Mittel über ~1000 Replikate/Jahr (4 × 250), stratifiziert nach Instrumenten-Regime, wobei Varianz zwischen Instrumenten explizit als Fitnessträger dient (Bet-Hedging-Formalismus).

**Existenz-Check:**
- 0DTE-Gamma-Ende-Reversion (fade close-flow / pin-unwind) ist Retail-Folklore und Dealer-Flow-Literatur dokumentiert (gexmetrix, zerogex, TradingWizard), allerdings nur als einzelnes Setup pro Tag auf SPX/ES — nicht als formaler Zwang-Replikat-Test über Instrumenten-Array.
- Geometrisches Mittel / Kelly / Bet-Hedging als Fitness-Kriterium existiert in Ökologie und Portfolio-Theorie (Kelly 1956; Thorp; Cover & Ordentlich; Entropy 2017, 19(2):82; arXiv 1904.04422), aber nicht als *Auswertelogik einer konkreten Zwang-Ereignisstudie* über ein Futures-Array.
- Cross-Instrument-Panels sind Standard-Diversifikation/Risiko-Reduktion — nicht als *primäres* Bet-Hedging-Strategie-Design, bei dem Varianz zwischen Instrumenten als Information gilt und das geometrische Mittel über instrumentenstratifizierte Zwang-Replikate das Erfolgsmaß ist.
- Kein Treffer, der alle drei Komponenten (kalenderfester 0DTE-Zwang + 4er-Futures-Array als Umgebungen + geometrisches Mittel über Replikate mit Varianz-als-Fitness) verbindet.

**Urteil:** NOVEL

Keine direkte publizierte Umsetzung — die Teilkomponenten (0DTE-Reversion, Kelly/geometrisches Mittel, Cross-Instrument-Diversifikation) existieren jeweils isoliert, aber die Kombination als Bet-Hedging-Replikat-Statistik über einen kalenderfesten Zwangs-Kanal in einem Futures-Array ist nicht besetzt.
