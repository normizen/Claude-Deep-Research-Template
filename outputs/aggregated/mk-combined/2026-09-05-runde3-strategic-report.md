# Strategic Innovation Report — 2026-09-05-runde3 (0DTE / Cross-Instrument)

**Cluster:** futures-trading-edge | **Rolle dieses Dokuments:** Assembly (kein Inhalt neu) | **Quellen:** siehe Anhang

---

## Executive Summary

Runde 3 verlagert die Zwangsmechanik-Suche von seltenen Einzelmarkt-Ereignissen (Opex, Prop-Flat) auf zwei neue Achsen: **tägliche Replikation** (0DTE-Gamma-Ende, ~250 Ereignisse/Jahr) und **Cross-Instrument-Arrays** (ES+NQ+GC+ZB als Messeinheit). Vier neue Axiome (A22–A25), vier Dogmen-Brüche (D21–D24). Zwei Generatoren (KIMI: 8 Ideen, OPUS: 7 Ideen) mit je zwei Advocati — kein Eigenfeld-Bias, OPUS-Feld dominiert inhaltlich. Einziger Kandidat, der die volle Feasibility passierte: **ID41o (0DTE-Close-Gamma-Reversions-Panel) — CONDITIONAL GO** mit drei verbindlichen Umbauten: 2+2-Panel statt 4 Replikate (GC/ZB haben kein homologes 16:00-Gamma-Ende → Falsifikator-Beine), Handel nur im oberen |GEX|-Quartil (Median-Tag trägt nach Kosten nichts), Overnight aus der Kernhypothese gestrichen. Effektive Replikate ehrlich nach unten korrigiert (~400/Jahr statt 1.000). ID52k wird als Metrik-Modul in ID41o absorbiert, ID43o/ID53o als Diagnostik-Module. Vorregistriertes Test-Design mit 6 Abnahmekriterien liegt test-fertig vor. Nächster Schritt: manueller QC-Run (~30 min, $0).

---

## 1. Neue Axiome/Dogmen

**Axiome:**
- **A22 — Settlement-Zwang (T+1):** erster reiner Kassa-Zwang, der via AP-Hedging kalenderfest in Index-Futures exportiert wird; Covariate, kein Outright.
- **A23 — 0DTE-Strukturwandel:** die Gamma-Dosis sitzt seit 2022 im täglichen 16:00-ET-Ende, nicht am Monats-Opex → ~250 Replikate/Jahr statt ~12; hebt ID30s Power-Problem.
- **A24 — Erntbarkeits-Filter (Meta):** ein Zwang ist Retail-erntbar gdw. (a) Retail-Größe, (b) terminliches Ende, (c) kein Latenz-Rennen; macht Kandidaten in 5 min klassifizierbar.
- **A25 — Instrumenten-Streuung > Zwangs-Streuung:** Bündelungs-Achse primär über unkorrelierte Underlyings (ES+NQ+GC+ZB), nicht über Zwänge eines Instruments.

**Dogmen-Brüche:**
- **D21** „Edge läuft auf einem Instrument" → Zwang ist Eigenschaft der Marktstruktur; der Test IST das Panel.
- **D22** „Basis/Arbitrage ist Retail unzugänglich" → die Arbitrage nicht ausführen, aber ihre Liquidierung ernten.
- **D23** „Rebalancing ist institutionelles Terrain" → das Futures-Echo des Settlement-Zwangs ist Retail-erntbar (kalenderfest, öffentlich).
- **D24** „REFUTED ist zeitlos" → Widerlegung gilt nur für Regime + Zeitgitter; REFUTED wird zu REGIME-STATUS mit Re-Trigger.

---

## 2. Seeds

- **Metamaterialien (Cluster 1, ∞ Tage ungenutzt):** die Einheit ist der falsche Messpunkt — Funktion entsteht aus dem Array. Liefert die Mess-Logik: Transferfunktion/Dispersion/Bandlücken des Instrumenten-Arrays statt Einzelmarkt-Signal.
- **Bet-Hedging (Cluster 2, ∞ Tage ungenutzt):** Fitness = geometrisches Mittel über Replikate, stratifiziert nach Umgebungstyp; Varianz zwischen Umgebungen ist Information. Liefert die Auswertelogik für die täglichen 0DTE-Replikate.

Beide Seeds erfüllten die ≥50 %-Nutzungspflicht in beiden Generator-Feldern; Kombinationslogik: D1 definiert *was* gemessen wird (Array-Antwort), D2 *wie* ausgewertet wird (Replikat-Verteilung).

---

## 3. ~~GENERATOR-A/B~~ **UNGÜLTIG — alle Subagenten liefen auf Kimi K3**

**KORREKTUR 2026-09-05:** Der hier dargestellte Modellvergleich fand technisch nicht statt (delegate_task ignoriert pro-Task-Modell-Pins; Dashboard bestätigte nur Kimi). Die untenstehenden Überlebensraten sind Kimi-gegen-Kimi mit zwei Rollen-Prompts — als Modellvergleich wertlos, als Dokumentation der beiden Ideenfelder aber lesbar. Die Ideen-Ergebnisse der Runde (ID41o CONDITIONAL GO etc.) sind davon NICHT betroffen.

### 3a. (Archiv, nicht als Modellvergleich lesen) Ehemalige 'A/B'-Darstellung

**Kreuz-Matrix (15 Ideen × 2 Advocati):** ✅ = überlebt (ggf. bedingt), ✗ = tot

| Idee | Feld | Kern | Advocatus 1 (OPUS) | Advocatus 2 (KIMI) |
|---|---|---|---|---|
| ID40k Array-Gamma-Dispersion | KIMI | Dispersion als primäres Signal | ✅ bedingt | ✅ |
| ID42k Settlement-Echo-Impuls | KIMI | T+1-Export als Array-Impuls | ✅ bedingt | ✗ (A19/Einpreisung) |
| ID44k Bet-Hedging-Replikat-Statistik | KIMI | Geo-Mittel-Metrik | ✅ | ✗ (Subst./D11) |
| ID46k Bandlücken-Detektor | KIMI | Nicht-Durchlass-Fenster | ✅ bedingt (mit Verwender) | ✗ (Wirtsignal) |
| ID48k Settlement-Rebalancing-Panel | KIMI | Quartals-Dispersions-Panel | ✅ | ✗ (Power) |
| ID50k Regime-Exhumierung ID26 | KIMI | ID26 unter 0DTE-Regime | ✅ bedingt | ✗ (D24-Missbrauch) |
| ID52k Cross-Instrument-Bet-Hedging | KIMI | 0DTE-Ende × 4 Instrumente, geo. Mittel | ✅ | ✅ (Panel-Kern) |
| ID54k Array-Bandlücken-Transfer | KIMI | Settlement moduliert 0DTE | ✅ | ✗ (Komplexität) |
| ID41o 0DTE-Close-Gamma-Panel | OPUS | Panel-Reversion am Zwangsende | ✅ (stärkste Idee) | ✅ |
| ID43o Settlement-Echo-Kovariate | OPUS | Array-Dispersion am Stichtag | ✅ bedingt | ✅ (Stratifikator) |
| ID45o Bandlücken-Karte | OPUS | Kohärenz-Timing-Layer | ✅ bedingt (mit 41o) | ✅ bedingt |
| ID47o Replikat-Stratifizierung | OPUS | Umgebungstyp-Strata | ✅ | ✗ (kein eigenes Signal) |
| ID49o Gerichtetes Rebalance-Echo | OPUS | NQ vs. ES Additions/Deletions | ✅ bedingt | ✗ (Einpreisung + Power) |
| ID51o Phänotypen-Portfolio | OPUS | Bet-Hedging-Sizing | ✅ | ✗ (Sizing-Layer) |
| ID53o Flip-Kohärenz-Test | OPUS | A25-Unabhängigkeits-Diagnostik | ✅ bedingt (mit 41o) | ✅ bedingt |

**Überlebensraten:** OPUS-Feld: 57 % (Advocatus KIMI) / 29 % (Advocatus OPUS: 41o, 53o klar; 43o, 45o nur bedingt) — KIMI-Feld: 25 % / 25 % (je 40k + 52k bzw. 44k + 52k). **Kein Eigenfeld-Bias:** beide Advocati töteten Ideen des eigenen Feldes im selben Maß wie fremde; die härtesten Einwände gegen OPUS-Ideen kamen vom OPUS-Advocatus (ID29-Overlap, Zirkelschluss-Risiko 53o) und umgekehrt.

**FAZIT Modellvergleich:** KIMI generiert konzeptuell breiter (mehr Dreifach-Kombis), aber 6/8 Ideen sind Metrik-Aufsätze, Filter-Umkleidungen oder Power-Leichen. OPUS ist straffer und ehrlicher (Power-Warnungen, Falsifikatoren, Erbschafts-Deklaration eingebaut) und liefert den einzigen Feasibility-Überlebenden (ID41o) plus die verwendergebundene Diagnostik (43o, 45o, 53o). KIMIs Überlebende (40k, 52k) sind in ID41o substanzabsorbierbar — kein Verlust durch Feld-Dominanz. **Generator-Override evaluieren:** das paritätische A/B-Setup hat hier keine komplementären Überlebenden produziert — OPUS allein hätte das Ergebnis getragen. Empfehlung: Runde 4 mit OPUS als Hauptgenerator + KIMI nur als Dogma-Break-Generator (sein D24-Missbrauch-Einwand war der schärfste Qualitätsfilter der Runde).

---

## 4. ID41o 0DTE-Close-Gamma-Panel — CONDITIONAL GO

**Idee:** Konditionierte Reversion am täglichen 0DTE-Gamma-Zwangsende (15:30→16:00 ET) über ES+NQ, mit GC/ZB als eingebautem Falsifikator. Novelty-Check: NOVEL (Cross-Instrument-Panel + vorregistrierte Signaturen unbesetzt; nächste Nachbarn: SSRN 4692190, SSRN 4881008).

### 3 verbindliche Umbauten

1. **2+2-Panel statt 4 Replikate:** ES/NQ = Test-Beine (echtes 16:00-0DTE-Ende); GC/ZB = Kontroll-/Falsifikator-Beine (kein homologes Gamma-Ende — treten sie gleich stark auf, ist der Effekt generischer Close-Flow → REFUTED als Gamma-Effekt). Replikate-Claim von 1.000 auf ~400/Jahr korrigiert.
2. **Nur oberes |GEX|-Quartil:** Cboe-Daten zeigen, der Median-Tag trägt nach 1-Tick-RT-Kosten nichts; Abstain-Architektur ist überlebensnotwendig, nicht optional.
3. **Overnight aus dem Kern gestrichen (A25):** nach 16:00 ist das Gamma tot — Overnight-Reversion wäre der eingepreiste generische Close-Effekt; nur noch explorative Nebenzeile.

### Größenordnungs-Gate

**Der Median trägt nichts — der Effekt lebt in der IQR.** Median-0DTE-Net-Gamma ist nur ein Bruchteil der Tagesliquidität (unterer Rand des marktbewegenden Bereichs); Whisker und oberes Quartil erreichen Größenordnungen, die eine Reversion nach Kosten tragen können. Konsequenz: der unkonditionierte Test wäre NO-GO gewesen — nur die Regime-Stratifizierung (Dosis-Response via Flip-Nähe + Top-Quartil-Filter) macht das Design lebensfähig.

### Test-Anleitung (vorregistriert, test-fertig)

**Code:** `outputs/individual/2026-09-05-runde3/code/qc_id41o_0dte_gamma_test.py` — eine QC-Research-Notebook-Zelle, manueller Run ~30 min, Kosten $0 (Daten in QC enthalten).

**Abnahmekriterien (identisch zur ID26-Konvention):**
1. Cliff's d (Panel-Mittel ES+NQ) **≥ 0,10**
2. Placebo-Perzentil (n=500, Nicht-Verfallstage gleiche Uhrzeit) **> 95 %**
3. **2+2-Falsifikator:** Cliff's d(Test vs. GC/ZB-Kontrolle) **> 0** — sonst REFUTED als Gamma-Effekt
4. **Decay-Split:** Effekt 2022+ vorhanden; 2019–2021 darf **nicht** existieren — sonst kein 0DTE-Phänomen
5. **Dosis-Response monoton** über Flip-Nähe-Quartile (Richtungsbedingung)
6. Multiplizität: Holm über Test-Beine; Abstain-Regeln (halbe Tage, Datenlücken, FOMC/CPI) vorab fixiert und gezählt

**Abbruch:** d < 0,10 oder Placebo ≤ 95 % → nicht bestanden, keine Nachfassung; GC/ZB gleiche Stärke → Gamma-Kanal beerdigt; 2019–2021 gleicher Effekt → REFUTED; Kostenquote > 15 % der Top-Quartil-Reversion → ökonomisch tot auch bei statistischem Signal.

---

## 5. Konsolidierungen

- **ID52k → Metrik-Modul von ID41o:** Trade deckungsgleich mit ID41o (gleiche Fenster, gleiche Richtung); einziger Beitrag ist der Bet-Hedging-Formalismus (geometrisches Mittel über Replikate, Regime-Stratifizierung) — als Auswertungs-Abschnitt [6] im ID41o-Protokoll übernommen, nicht als eigenständige Idee (Eigenständigkeits-Gate verfehlt; Konsistenz mit ID47o/ID51o-Präzedenz).
- **ID43o → Diagnostik-Modul:** Fenster-Feinlokalisierung (5-Min-Sub-Raster 15:45→16:00) als Add-on-Zelle nach ID41o-Bestand; kein eigenes Signal. Novelty: NOVEL (Z-Score-Dispersions-Spread über 4 Futures-Klassen unbesetzt).
- **ID53o → Diagnostik-Modul:** ES/NQ-Replikat-Korrelation (effektive Replikatzahl = n·(1−ρ)/(1+ρ)) für ehrliche Power-Angabe im ID41o-Protokoll; prüft A25s Unabhängigkeitsannahme empirisch. Novelty: NOVEL (Signal-Kohärenz als Panel-Validierung nicht publiziert).
- **ID30-Parallele / D24:** ID26/ID30 scheiterten an Dünnheit über alle Tage gemittelt (D24 unkonditioniert). ID41o ist die direkte Antwort: gleicher Statistik-Apparat, konditioniert auf strukturell neuen Zwang im oberen Quantil. Besteht ID41o → D24 präzisiert (unkonditioniert gültig, konditioniert nicht). Scheitert ID41o → D24 final bestätigt und das Close-Reversions-Forschungsprogramm kann geschlossen werden.

---

## 6. Nächste Schritte

1. **QC-Run ID41o** (manuell, ~30 min): Notebook-Zelle ausführen, Ergebnis-Report analog `id26/run1.txt` ablegen.
2. **Bei Bestand:** ID43o-Sub-Fenster-Scan und ID53o-Korrelations-Diagnostik als Add-ons; danach ID40k-Dispersion als Erweiterung; ID45o-Timing-Layer optional.
3. **Bei Nichtbestand:** D24 final bestätigt; Close-Reversions-Programm schließen; Cluster-Fokus zurück auf ID29-Bündelung (A22-Settlement-Covariate dort nutzen).
4. **Prozess:** Generator-Setup für Runde 4 neu gewichten (OPUS-Hauptgenerator, KIMI Dogma-Break/Advocatus); Cluster-Memory (`projects/futures-trading-edge/`) mit A22–A25, D21–D24 und den Ideen-Outcomes aktualisieren.

---

## Anhang: Datei-Index

**Scratchpad (Generierung/Advokatur):**
- `scratchpad/2026-09-05-runde3-axioms.md` — A22–A25 + verworfene Kandidaten-Räume
- `scratchpad/2026-09-05-runde3-dogma-break.md` — D21–D24
- `scratchpad/2026-09-05-runde3-domain-selection.md` — Anti-Anchor, Seed-Wahl
- `scratchpad/2026-09-05-runde3-discovery-draft-KIMI.md` — Generator A, 8 Ideen (40k–54k)
- `scratchpad/2026-09-05-runde3-discovery-draft-OPUS.md` — Generator B, 7 Ideen (41o–53o)
- `scratchpad/2026-09-05-runde3-feasibility-pre-KIMI.md` — Advocatus KIMI (Urteile über beide Felder)
- `scratchpad/2026-09-05-runde3-feasibility-pre-OPUS.md` — Advocatus OPUS (Urteile über beide Felder)

**Outputs (Prüfung/Design):**
- `outputs/individual/2026-09-05-runde3/novelty-check-id41o.md` — NOVEL
- `outputs/individual/2026-09-05-runde3/novelty-check-id43o.md` — NOVEL
- `outputs/individual/2026-09-05-runde3/novelty-check-id52k.md` — NOVEL
- `outputs/individual/2026-09-05-runde3/novelty-check-id53o.md` — NOVEL
- `outputs/individual/2026-09-05-runde3/feasibility-id41o.md` — CONDITIONAL GO (4 Gates)
- `outputs/individual/2026-09-05-runde3/feasibility-id52k.md` — MODUL-VON-ID41o
- `outputs/individual/2026-09-05-runde3/experiment-designs.md` — vorregistriertes Test-Design, Abnahmekriterien
- `outputs/individual/2026-09-05-runde3/code/qc_id41o_0dte_gamma_test.py` — QC-Notebook-Zelle
