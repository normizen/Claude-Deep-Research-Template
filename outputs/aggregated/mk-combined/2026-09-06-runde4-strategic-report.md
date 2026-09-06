# Strategic Innovation Report — 2026-09-06-runde4 (Breite: Settlement-/Anker-Mechanik)

## Executive Summary

Nach drei Zwangs-Toten (ID26, ID29, ID41o — alle an A24-Erntbarkeit gestorben) öffnet Runde 4 den Raum jenseits der Tagesende-/Verfalls-Zwangsmechanik: Die Settlement-/Anker-Struktur selbst wird zum Träger (A28: Auction/Continuous-Bruchlinie). Erste echte A/B-Runde des Clusters: zwei vollständige Generator-Felder (KIMI, OPUS) unter identischen Axiomen und Seeds — erste Messung der Modell-Differenz möglich. Konsens-#1 beider Advocati und beider Felder: **ID67o (Batch-minus-Marginal-Residual, BMR)** — GO, konditional auf Daten-Mapping und Guard-Überlebensrate ≥ 15 %. Test-Code liegt vor (QC, SETTLEMENT_CSV als Pflicht-Input). ID61o fällt durch einen externen Fund (Auction-Echo publiziert) zurück auf die Staffelungs-Variante; ID63o bleibt NOVEL, hängt aber an der ID67o-Settlement-Pipeline. Nächste Priorität: ID67o-Lauf; ID61o-Redesign erst nach Feasibility-Neuauflage.

## 1. Neue Axiome/Dogmen

- **A26** — Arbitrage-Resistenz ohne Zwang: Effekte leben in Horizont-Spalten, für die keine Arbitrage-Population existiert.
- **A27** — Teilnehmerstruktur-Lead-Lag ist mechanisch (Diffusion über Populationen), nicht statistisch (Kointegration) — nur als Kontext, nicht als Renn-Signal.
- **A28** — Auction- vs. Continuous-Modus haben verschiedene Informations-Ökonomien; die Anker-Differenz ist Messgröße, nicht Fehler.
- **A29** — Repräsentations-Vorsprung: Edge liegt auf der Ebene, die Standard-Pipelines wegglätten (Settlement ≠ QC-Daily-Close).
- **A30** — Regime persistieren durch prozyklische Selbstverstärkung der Teilnehmerstruktur; Nutzen = regime-bedingte Strategie-Auswahl.
- **A31** — Haltezeit 2 h–3 Tage ist die konkurrenzfreie Retail-Achse; Signalhorizont darf länger sein als die Position.
- **D25** — „Edge im Einzelinstrument" gebrochen: die Ereignis-Dimension liegt zwischen Instrumenten/Modi.
- **D26** — „Intraday-Sub-Tick = Rauschen" gebrochen: Rundung ist deterministisches Marktdesign (mode-form, nicht race-form).
- **D27** — Cross-Asset-Information statt Cross-Asset-Trade: Kreuz-Signal konsumieren, nur ein Bein tragen.
- **D28** — Portfolio mechanisch unabhängiger Kleineffekte statt Suche nach dem einen großen Edge.

## 2. Seeds

**Schelling-Punkte (Cluster 5, nie verwendet):** Koordination ohne Kommunikation über saliente Brennpunkte — Settlement-Zeiten, runde Zahlen, Auktionstermine als regelfeste Focal Points.
**Sparse Coding (Cluster 3, nie verwendet):** Effizienz durch Ausschaltung — wer nach dem Anker noch aktiviert, handelt aus Meinung, nicht aus Referenzpflicht; Aktivierungs-Sparsity als Effektstärke-Modulator.
Vereinigung: Ordnung an Modus-Übergängen, wenn Populationen asynchron auf gemeinsam erwartete Koordinationspunkte konvergieren.

## 3. ERSTE ECHTE A/B

Erste Runde mit zwei vollständig getrennten Generator-Feldern unter identischem Setup — Kreuz-Matrix ermöglicht Modellvergleich auf vier Achsen (Vorzeichenquelle, Artefakt-Kontrolle, Kosten-Quantifizierung, Abgrenzungsdisziplin).

- **Konsens-#1:** ID67o ist Rang 1 in beiden Feldern — KIMI („SURVIVE — Top") und OPUS („ÜBERLEBT — stärkste Idee beider Felder").
- **Generator:** OPUS > KIMI — erste echte Messung dieser Differenz. OPUS behandelt systematisch zwei Fehlerklassen, die KIMI nicht sieht: (1) ob das Vorzeichen aus dem Mechanismus folgt oder aus dem eigenen Return des gehandelten Instruments, (2) Artefakt-Kontrolle (Rundung, Anker-vs-Wanduhr, mechanismus-spezifischer Placebo). Pins/Anker-Zeiten wurden von OPUS gegen Primärquellen verifiziert (CME-Wiki, CFTC-Filings), nicht aus dem Gedächtnis übernommen.
- **Advocatus:** KIMI kompakt und entscheidungsstark (klare Duell-Logik, ID64k fällt gegen ID67o); OPUS operationalisierbar mit Pflicht-Umbauten (Rundungs-Symmetrie, Überlebensraten-Gate, Bounce-Konfundierung bei ID69o — „gefährlich scharfes Messer mit stumpfer Klinge").
- **Hinweis:** Eine A/B-Runde ist eine Messung, kein Urteil — 2–3 weitere Dual-Runden zur Bestätigung der Modell-Differenz einplanen.

## 4. ID67o BMR — GO (konditional)

**Mechanik:** BMR = offizielles CME-Settlement (30-s-VWAP, gerundet auf 0,25) − Close des letzten Minutenbars vor dem Anker (14:59 CT). sign(BMR) bei |BMR| ≥ Guard prognostiziert die RTH-Erststunde des Folgetags.

### 3 Gate-Lösungen

1. **Rundungsfalle → Symmetrie:** Treatment aus der öffentlichen CME-Settlements-Seite (nicht aus QC — QC-Daily-Close ist letzter Trade, nicht Settlement); Pseudo-Anker-Placebo identisch konstruiert und identisch auf 0,25 gerundet, plus Guard-Kohorte |d| ≥ 0,25.
2. **Überlebensrate → Abbruchregel:** Erster Code-Schritt vor jeder Inferenz: Verteilung |BMR| tabellieren; Überlebensrate bei Guard 0,5 (ES) / 1,0 (NQ) < 15 % → Guard auf ein Rundungs-Quantum senken; auch dort < 15 % → **NO-GO ohne Haupttest**.
3. **Kontrolle → dreistufig:** 500 blockweise Vorzeichen-Permutationen (Monatsblöcke); Jonckheere-Monotonie über Monatsend-Strata (kalenderfest, kurvenanpassungsfest); GC als Placebo-Anker, ZB als Rundungs-Falsifikator mit eigener 1/64-Rundung.

### Novelty

**PARTIALLY** — Komponenten bekannt (Settlement-VWAP-Mechanik, Gap-Trading, Expiration-Effekte), aber kein publiziertes Retail-Signal registriert „Settlement − letzter Continuous-Preis" als konditionierten Folgetag-Reversal-Filter; die Formalisierung als BMR ist neu.

### Test-Anleitung (Checkliste)

- [ ] **SETTLEMENT_CSV befüllen:** offizielle Settlements von der CME-Settlements-Seite (E-Mini S&P 500 / Nasdaq-100, CSV-historisch) per Datum + Lead-Month laden; defensive Abfrage mit Fallback + Warnung ist im Code.
- [ ] **Vorab-Validierung:** 20-Tage-Stichprobe — CME-Settlement ≠ QC-Daily-Close, Differenz auf 0,25-Grid (sonst Feld gelöscht, Test sinnlos).
- [ ] **Abbruchregel zuerst:** Überlebensraten-Tabelle vor Haupttest; < 15 % auf Rundungs-Quantum → kein Inferenztest, klare NO-GO-Ausgabe.
- [ ] **Falsifikatoren lesen:** GC nicht signifikant; ZB-Effekt nur auf 1/64-Grid — ein „Effekt" in ZB auf dem ES-Grid beweist die Rundungsfalle und bestätigt den Guard.
- [ ] Code: `outputs/individual/2026-09-06-runde4/code/qc_id67o_bmr_test.py`; Output im run1.txt-Format (Handelstage, Abstain-Tage gezählt).

## 5. Zurückgestellt

- **ID61o (Anker-Staffel-Kaskade):** VCG-Fund („The 1PM Echo", 2026) — die Auction-Echo-Variante ist publiziert und **positiv** belegt; sie ist damit als eigenständige, extern validierte Kante zu vermerken (nicht vom Cluster erntbar als Novelty, aber als Marktfakt). Redesign nötig zur Staffelungs-Variante: tägliches 14:00–15:00-CT-Fenster zwischen ZB- und ES-Verankerung als kalenderfestes Lead-Lag. Advocatus-Einwand (Vorzeichen-Regime-Instabilität, Aktien-Anleihen-Korrelations-Flip 2022) verschärft sich dort; neues Feasibility-Dokument vor Code.
- **ID63o (Post-Anker-Sparse-Fenster):** NOVEL (unter Vorbehalt — Such-Backend teilweise ausgefallen), hängt aber an derselben Settlement-Datenpipeline wie ID67o; sinnvolle Reihenfolge: erst ID67o-Lauf (validiert Mapping + Infrastruktur), dann ID63o als Folgetest. Earnings-Kontamination bleibt dominanter Risikofaktor — print-freie Kohorte ist Pflicht-Umbau. Achtung (OPUS): PAR und BMR teilen den Settlement-Term mit entgegengesetztem Vorzeichen — 63o und 67o sind rechnerisch nicht unabhängig und dürfen nicht als zwei Wirte in ein D28-Portfolio gezählt werden.

## 6. Nächste Schritte

1. **ID67o-Lauf:** SETTLEMENT_CSV befüllen, QC-Notebook laufen lassen, Abbruchregel beachten (~1 h manueller Datenaufbereitung, ≤ 50 $ Gesamtkosten).
2. **ID64k als eingebaute Benchmark im selben Notebook** mitlaufen lassen (gleiche Daten, nahe null Zusatzkosten) — entscheidet mit, ob der A29-Repräsentations-Vorsprung trägt oder generisches Schlussstunden-Reversal.
3. **ID61o-Redesign:** Staffelungs-Variante mit vorregistrierter Vorzeichen-Regel an langsamer externer Regime-Variable; Rundungs-Guard auf BMR_ZB übertragen; neues Feasibility-Dokument.
4. **ID69o-Umbau:** Vorhersage bounce-bereinigt formulieren, bevor das Modul Beerdigungs-Vollmacht über die Überlebenden bekommt.
5. **A/B-Dual beibehalten:** 2–3 weitere Dual-Runden zur Bestätigung der Modell-Differenz (Generator OPUS > KIMI).
6. Cluster-Memory: VCG-Auction-Echo als extern validierte Kante in `idea-outcomes.md` vermerken.

## Anhang: Datei-Index

| Datei | Inhalt |
|---|---|
| `scratchpad/2026-09-06-runde4-axioms.md` | A26–A31, Tragfähigkeits-Ranking |
| `scratchpad/2026-09-06-runde4-domain-selection.md` | Seed-Auswahl (Schelling × Sparse Coding) |
| `scratchpad/2026-09-06-runde4-discovery-draft-KIMI.md` | Generator A: ID60k–ID70k |
| `scratchpad/2026-09-06-runde4-discovery-draft-OPUS.md` | Generator B: ID61o–ID73o, Anker-Landkarte |
| `scratchpad/2026-09-06-runde4-feasibility-pre-KIMI.md` | Advocatus A (kompakt, Duell-Logik) |
| `scratchpad/2026-09-06-runde4-feasibility-pre-OPUS.md` | Advocatus B (Pflicht-Umbauten, A/B-Fazit) |
| `outputs/individual/2026-09-06-runde4/novelty-check-id67o.md` | PARTIALLY NOVEL |
| `outputs/individual/2026-09-06-runde4/novelty-check-id61o.md` | Auction-Echo belegt (VCG), Staffelung novel |
| `outputs/individual/2026-09-06-runde4/novelty-check-id63o.md` | NOVEL unter Vorbehalt |
| `outputs/individual/2026-09-06-runde4/feasibility-id67o.md` | GO konditional, 3 Gates, Test-Design |
| `outputs/individual/2026-09-06-runde4/experiment-designs.md` | Abnahmekriterien, Zurückstellungen |
| `outputs/individual/2026-09-06-runde4/code/qc_id67o_bmr_test.py` | Test-Code (QC) |
