# Experiment-Designs — Runde 3 (2026-09-05)

**Rolle:** Implementation Designer | **Status:** vorregistriert, test-fertig
**Primär-Code:** `code/qc_id41o_0dte_gamma_test.py` (QC-Research-Notebook, eine Zelle)

---

## ID41o — 0DTE-Close-Gamma-Reversions-Panel (Hauptdesign, CONDITIONAL GO umgesetzt)

### Axiom-Basis

| Axiom | Aussage | Tragfähigkeit für ID41o |
|---|---|---|
| **A23** | Zwangsflüsse (kein freiwilliger Handel) hinterlassen vorhersagbare Preisspuren, weil die Gegenseite Liquidität gegen Prämie bereitstellt. | MM-Gamma-Hedging am 0DTE-Verfall ist definitionsgemäß zwangsläufig — die Prämie ist die Reversion. |
| **A24** | Die Stärke eines Zwangs skaliert mit seiner Größe relativ zur verfügbaren Liquidität, nicht mit seiner absoluten Größe. | Begründet Umbau 2: Median-0DTE-Net-Gamma ($173mm/1% vs. ~$400bn Tagesliquidität) trägt nichts; nur oberes Quartil handelbar. |
| **A25** | Ein Zwangseffekt existiert nur in dem Zeitfenster, in dem der Zwang wirkt; danach ist jede Fortsetzung ein anderer (eingepreister) Effekt. | Begründet Umbau 3: 0DTE-Gamma ist 16:00 ET tot → Overnight aus Kern gestrichen; Kern = letzte ~30 RTH-Minuten des Verfallstags selbst. |

### Dogmen-Dekonstruktion

| Dogma | Dekonstruktion |
|---|---|
| **D21** ("Mehr Replikate = besser") | GC/ZB liefern **kein** homologes 0DTE-Ende (Gate 4, Feasibility). 4-Replikate-Panel wäre Scheinpräzision. → 2+2: GC/ZB werden vom Pseudo-Replikat zum eingebauten **Falsifikator** — ihr Fehlschlag stärkt das Design, ihr Mitlaufen widerlegt es. |
| **D24** ("Intraday-Reversion ist nicht erntbar nach Kosten") | ID26 bestätigte D24 für das **unkonditionierte** Fenster (corr −0,045, d=0,159 scheiterte am Placebo). 0DTE-Gamma-Ende ist die erste strukturell neue Kraft in diesem Fenster seit 2022 — der Effekt lebt im oberen Quantil (A24), wo D24 nie getestet wurde. Siehe ID30-Parallele unten. |

### Mechanik-Kern

Market Maker sind am Verfallstag netto long/short 0DTE-Gamma. In den letzten ~30 RTH-Minuten (15:30→16:00 ET) hedgent sie zwangsläufig in ES/NQ-Futures: positives Gamma → Counter-Trend-Hedging → **verstärkt intraday Reversion** (Dim/Eraker/Vilkov 2023, mechanisch bestätigt; SSRN 4881008: Kanal läuft über Index-Futures). Um 16:00 verfällt das Gamma; der letzte Hedging-Baustein ist der einzige Zeitpunkt, an dem der Zwang zeitscharf, täglich replizierbar und seit 2022 strukturell neu ist.

### Die 3 verbindlichen Umbauten (exakt umgesetzt)

1. **2+2-Panel statt 4-Replikate:**
   - **Test-Beine:** ES (SP_500_E_MINI), NQ (NASDAQ_100_E_MINI) — echtes 16:00-0DTE-Gamma-Ende.
   - **Kontroll-/Falsifikator-Beine:** GC, ZB — kein homologes 0DTE-Ende; dort **darf** der Effekt nicht auftreten. Tritt er dort gleich stark auf → generischer Close-Flow → **REFUTED als Gamma-Effekt**.
   - Effektive Replikate: **~400 echte/Jahr** (2 Test-Beine × ~200 Verfallstage, Korrelation ES/NQ ehrlich eingerechnet), davon ~100 im oberen Gamma-Quartil. Der 1.000-Replikate-Claim ist beerdigt.

2. **Nur oberes |GEX|-Quartil handelbar:**
   - Cboe-Beleg: Median-0DTE-Net-Gamma = 0,04–0,17% der Tagesliquidität → trägt nach 1-Tick-RT-Kosten nichts. Signal **nur aktiv**, wenn Tages-Net-Gamma im oberen IQR.
   - Implementierung (Code): look-ahead-freier Regime-Proxy (rollierender 60d-Median des Zwangsfenster-Betrags, `shift(1)`), Top-Quartil = handelbar; Rest = Abstain (ausgeschlossen **und gezählt**, Datenfalle 4).
   - **Dosis-Variable:** Flip-Level-Nähe als ordinaler Prädiktor (Quartil-Bins 0–3); vorregistriert: Reversion steigt monoton mit Dosis.

3. **Overnight GESTRICHEN aus Kern-Hypothese (A25):**
   - Kern-Zelle: letzte ~30 RTH-Minuten vor Verfall-Close → Reversion in den letzten Minuten des Verfallstags selbst (Erste-Hälfte 15:30–15:45 vs. Letzte-Hälfte 15:45–16:00, ID26-V2-Logik).
   - Overnight (16:00 → Folgetag 09:30) nur als **explorative Nebenzeile**, im Code und Protokoll klar als *eingepreist/generischer Close-Effekt* markiert — kein Abnahmekriterium.

### Alpha-Vorteil (warum Retail hier eine Chance hat)

Der grobe intraday SPX-Reversionsanteil ist bepreist (Dim/Eraker/Vilkov, Cboe, Amaya/Vasquez — institutionelle MM-Positionsdaten). **Nicht** bepreist im Retail-Zugriff: das vorregistrierte 2+2-Falsifikator-Panel mit Dosis-Response und Decay-Split. Der Retail-Vorteil ist kein Informationsvorteil, sondern ein **Selegtionsvorteil**: Abstain an ~75% der Tage + Micro-Kontrakte (MES/MNQ) machen die kleine Prämie überhaupt erst kosten-tragbar. Institutionelle müssen das volle Gamma-Buch fahren; Retail darf wählen.

### Abnahmekriterien (vorregistriert, identisch zur ID26-Konvention)

| # | Kriterium | Hürde |
|---|---|---|
| 1 | Cliff's d, Panel-Mittel (ES+NQ) vs. Null-Pool | **≥ 0,10** |
| 2 | Placebo-Perzentil (n=500, Nicht-Verfallstage gleiche Uhrzeit) | **> 95%** |
| 3 | **2+2-Falsifikator-Logik:** Cliff's d(Test vs. GC/ZB-Kontrolle) | **> 0** — sonst REFUTED als Gamma-Effekt (generischer Close-Flow) |
| 4 | Decay-Split: Effekt 2022+ vorhanden; **2019–2021 darf NICHT existieren** | Vorzeichen/Magnitude-Bedingung |
| 5 | Dosis-Response monoton (Flip-Nähe 0→3) | Richtungsbedingung |
| 6 | Multiplizität: Holm über Test-Beine; Abstain-Regeln (halbe Tage, Datenlücken, FOMC/CPI-Flag) vorab fixiert | — |

### Abbruchkriterien

- d < 0,10 **oder** Placebo ≤ 95% → NICHT BESTANDEN, keine Hypothesen-Nachfassung (Datenfalle 5).
- GC/ZB zeigen gleiche Stärke → Gamma-Kanal REFUTED, Design nicht retten durch Umparametrisierung.
- 2019–2021 zeigt gleichen Effekt wie 2022+ → kein 0DTE-Phänomen → REFUTED.
- Kostenquote > 15% der erwarteten Reversion im Top-Quartil → ökonomisch tot, auch bei statistischem Signal.

### Kosten

| Position | Betrag |
|---|---|
| QC-Cloud (bestehender Zugang, NDX/Gamma+OI+IV) | $0 |
| Daten (Minutenbars ES/NQ/GC/ZB via `qb.add_future`, backadjusted) | $0 (in QC enthalten) |
| Manueller QC-Run durch User | ~30 Min |
| **Gesamt** | **≤ $50-Budget, faktisch $0** |

---

## ID43o — Diagnostik-Modul: Fenster-Feinlokalisierung (kurz)

**Frage:** Liegt die Reversion gleichmäßig über 15:45→16:00 oder konzentriert in den letzten 5 Minuten? **Design:** Innerhalb des ID41o-Samples Sub-Fenster-Scan (5-Min-Raster, vorab fixiert: 15:45/15:50/15:55/16:00), Cliff's d pro Sub-Fenster, Holm-Korrektur. **Zweck:** Order-Timing-Optimierung nur *nach* ID41o-Bestand — kein eigenes Signal, keine Hürde. Läuft als Add-on-Zelle auf demselben Panel-DataFrame.

## ID53o — Diagnostik-Modul: ES/NQ-Replikat-Korrelation (kurz)

**Frage:** Wie unabhängig sind die 2 Test-Beine wirklich? **Design:** Pearson/Spearman der täglichen ES_rev- und NQ_rev-Scores im Analyse-Sample; effektive Replikatzahl = n·(1−ρ)/(1+ρ). **Zweck:** ehrliche Power-Angabe im ID41o-Protokoll (Feasibility schätzte ~350–400 statt 400–500). Output: eine Zahl + Konfidenzintervall, keine Handelsentscheidung.

## ID52k — Metrik-Modul: Bet-Hedging (Auswertung, keine eigene Idee)

**Definition:** Geometrisches Mittel der Wett-Quote über Replikate: `geo = exp(mean(log(1 + r_rev/|r_zwang|))) − 1`, stratifiziert nach Decay-Regime (2019–2021 vs. 2022+). **Einbettung:** Abschnitt [6] im ID41o-Code und Protokoll — bewertet, ob die Reversion als "Wette gegen den Zwang" kapital-effizient ist (Kelly-relevant), **nicht** ob sie existiert. Keine eigenen Abnahmehürden.

## ID30-Parallele — 0DTE löst das alte Power-Problem (D24)

ID26/ID30 scheiterten nicht am Fehlen von Reversion, sondern an deren **Dünnheit über alle Tage gemittelt** (D24: unkonditionierte Intraday-Reversion nicht erntbar). ID41o ist die direkte Antwort: derselbe Statistik-Apparat (Placebo n=500, Cliff's d ≥ 0,10, Decay-Split, Abstain-Zählung), aber konditioniert auf einen **strukturell neuen, zeitscharfen Zwang** im oberen Quantil. Falls ID41o bestünde, wäre D24 nicht falsch, sondern präzisiert: *unkonditioniert* gilt es weiter — konditioniert auf 0DTE-Gamma-Ende evtl. nicht. Falls ID41o scheitert, ist D24 mit der stärksten verfügbaren Konditionierung final bestätigt und das gesamte Close-Reversions-Forschungsprogramm kann geschlossen werden.

---

**Vorab-Registrierung:** Alle Hürden, Fenster, Filter und Falsifikator-Regeln stehen in diesem Dokument und im Code-Header **vor** der ersten Ausführung. Ergebnis-Report-Format: analog `outputs/individual/2026-09-03-pilot/test_results/id26/run1.txt`.
