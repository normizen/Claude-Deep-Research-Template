# Dogma-Graveyard — aktien-retail-edge

Dogmen sind Überzeugungen, Heuristiken oder Praktiken, die so weit verbreitet sind,
dass ihre Befolgung keinen Vorteil mehr bietet — weil alle es tun.

**Kernkriterium:** Nicht "ist es falsch?", sondern "ist es eingepreist?"
Ein Dogma kann wahr und trotzdem wertlos sein, wenn alle danach handeln.

Volltext mit Ursprung, Einpreisungs-Analyse und axiomatischer Prüfung:
`scratchpad/2026-08-30-aktien-retail-edge-strategic-dogma-break.md`

---

## Übersicht — 20 Dogmen (Session 2026-08-30)

| Nr | Dogma | Herkunft |
|---|---|---|
| D1 | "Retail ist strukturell im Nachteil, daran ist nichts zu ändern" | User |
| D2 | "Wer gewinnt, hat schnellere Infos oder Insiderwissen" | User |
| D3 | "Man braucht ein gutes Händchen — das hat man oder nicht" | User |
| D4 | "Technische Chartanalyse ist der Weg zum kurzfristigen Handel" | User |
| D5 | "Claude darf/kann mir nicht sagen, was ich konkret tun soll" | User (Fehldiagnose) |
| D6 | "Bei kleinem Kapital braucht es hohes Risiko für relevante Gewinne" | User |
| D7 | "Verluste begrenzen, Gewinne ausbauen" | User |
| D8 | "Langfristig schlägt kurzfristig" | User |
| D9 | "Niedrig = günstig, hoch = teuer" | User |
| D10 | "Diversifizieren schafft Sicherheit" | User |
| D11 | "Backtest-Erfolg zeigt echten Edge an" | Frontier-Scan + Futures-Cluster D7 |
| D12 | "Stop-Loss-Order = definiertes Risiko" | Geerbt (Futures D4), vertieft |
| D13 | "Mehr Daten/Informationen = bessere Entscheidung" | Geerbt (Futures D6) |
| D14 | "Trend is your friend" | Geerbt (Futures D5) |
| D15 | "Edge Decay ist bei allen Strategien unvermeidlich" | Geerbt (Futures D3) |
| D16 | "Retail sollte keine komplexen Systeme bauen — keep it simple" | Geerbt (Futures D9) |
| D17 | "Edge muss geheim gehalten werden" | Geerbt (Futures D8) |
| D18 | "Trading erfordert Präsenz zur Marktzeit" | **NEU** — Phase 1 |
| D19 | "Kleine, unbekannte Firmen sind schwerer/riskanter zu analysieren" | **NEU** — Phase 1 |
| D20 | "Ein Analyse-Report ist gleichbedeutend mit Handlungsfähigkeit" | **NEU** — Phase 1, Wurzelursache von D5 |

---

## Die entscheidungsrelevanten Gegenthesen

### D1 — Retail-Nachteil
Retail ist nicht pauschal im Nachteil, sondern segmentabhängig positioniert: im Large-Cap-/
optionsliquiden Segment strukturell unterlegen (Futures-A1/A9), im unterversorgten Small-/
Midcap-Segment strukturell **im Vorteil** (A4 Coverage-Ökonomie, A5 Market-Impact).

### D5 — "Claude darf nicht"
Nicht "Claude kann keine Handlungsanweisung geben", sondern: Claude kann ein explizites,
regelbasiertes Entscheidungssystem bauen, das der User selbst anwendet. Die Anwendung im
Einzelfall bleibt beim User — das System selbst darf so konkret sein wie mathematisch
möglich: exakte Schwellwerte, exakte Positionsgrößen-Formeln, exakte Abbruchbedingungen.

### D6 — Kleines Kapital braucht hohes Risiko
Die Stellschraube ist nicht das Risiko pro Trade, sondern (a) die Trefferqualität des
Mechanismus über die A4-Segmentwahl und (b) eine Positionsgrößen-Formel mit konsistenter
Reinvestitions-/Compounding-Logik statt Vergrößerung pro Trade.

### D11 — Backtest zeigt Edge
Backtesting ist notwendig, aber nicht hinreichend. Entscheidend: Was ist der strukturelle
Mechanismus, der den Edge erzeugt, und ist er noch aktiv? **Mechanismus zuerst, Backtest
als Plausibilitätsprüfung — nicht umgekehrt.**

### D12 — Stop-Loss = definiertes Risiko
Definiertes Risiko entsteht durch Positionsgrößen-Bemessung, die ein realistisches Gap-
Szenario einpreist (Größe so wählen, dass selbst ein 2–3-fach größerer Verlust als der
Stop-Abstand im Risikobudget bleibt). Die Stop-Order bleibt Ausführungsmechanismus, ist
aber nicht selbst die Risikogrenze. **Direkte Konsequenz für die harte User-Grenze.**

### D18 — Präsenz zur Marktzeit
Der Prozess ist strukturell asynchron ausführbar: Analyse und Entscheidung außerhalb der
Marktzeit, Ausführung über vorab platzierte bedingte Orders statt Echtzeit-Reaktion.
Passt direkt auf die harte Design-Grenze 1–2 h/Tag.

### D19 — Kleine Firmen schwerer analysierbar
Small-/Midcaps sind nicht schwerer zu bewerten, sondern erfordern, dass die Bewertungsarbeit
selbst geleistet wird statt Analystenkonsens zu übernehmen. Mehraufwand, kein Erkenntnis-
hindernis — und genau der Raum, in dem A4/A5 einen Vorteil begründen.

### D20 — Report = Handlungsfähigkeit
Handlungsfähigkeit entsteht nicht aus besserer Analyse, sondern aus einer zusätzlichen
expliziten Schicht: Schwellwerte, Sizing-Formel, Abbruchkriterien. Eine Entscheidungs-
architektur, die auf der Analyse aufsetzt, aber nicht aus ihr folgt.
