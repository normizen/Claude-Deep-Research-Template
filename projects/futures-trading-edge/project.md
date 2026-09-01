# Cluster: futures-trading-edge

## Thema
Strukturelle und mechanische Edges im Futures Day Trading (ES-mini, NQ-mini) — für Retail-Trader implementierbar.

## Status
Aktiv — **Prüfphase abgeschlossen, Neuausrichtung offen** (Stand 2026-09-02)

---

# STAND — bitte zuerst lesen

**Zeitraum der Arbeit:** 2026-08-30 bis 2026-09-02, vier Tage.

## Die Ausgangsfrage

*„Hat der VPIN-Regime-Filter Mehrwert fürs Trading?"* — und in der Folge: Tragen die
drei NOVEL-Ideen aus Session 2026-04-15 (GTZI, GEX-Topologie-Karte, SGM) einen
messbaren Vorteil?

## Die Antwort: viermal geprüft, viermal kein Signal

| Ansatz | Stichprobe | Ergebnis | Schärfstes Maß |
|---|---|---|---|
| **VPIN-Regime-Filter** | 7.003 Ereignisse, 4,5 Jahre | kein Effekt | Cliff's d −0,007 bis +0,003 (Kriterium 0,10) |
| **GEX-Walls** | 1.430 gegen 1.459 Placebo | kein Effekt über Placebo | Cliff's d < 0,03 |
| **GEX-Topologie** | 1.387 Tage, 3 Typen | 2 von 4 Vorhersagen, Effekte ~0 | max Cliff's d 0,051 |
| **Gamma-Regime** | 900 gegen 530 Tage | kein Effekt | max Cliff's d 0,073 |

**GTZI** ist nicht eigenständig testbar — es ist ein Filter und braucht ein Wirtssignal.
Als Messgröße funktioniert es (Streuung 0,26, 12 % unter 0,5), aber die Ereignisrate von
0,08 je Tag ist für Statistik zu niedrig.
**SGM** wurde über die Wall-Messung teilweise mitgeprüft, ohne Signal.

## Der eine belastbare positive Befund

**NDX kehrt intraday zurück — dreifach unabhängig gemessen:**
- VA-Ausbrüche: 97,5 % Reversion binnen 100 Dollar-Bars, MFE/MAE ≈ 1,00
- Wall-Kontakte: Median-Rendite negativ, aber am Placebo genauso
- Varianzverhältnis: 0,86 bis 0,91 in **allen** Topologie-Gruppen (1,0 = Zufallslauf)

**Daraus folgt aber kein Vorteil.** Direkt geprüft: Gegen die Ausbruchsrichtung zu handeln
liefert Median −0,75 bis −4,88 Punkte und eine Trefferquote von 47,8 bis 48,5 %. Die
Rückkehr ist real, aber nicht ernte-fähig.

## Was an Infrastruktur bleibt — der eigentliche Ertrag

| Baustein | Ort | Zustand |
|---|---|---|
| Value-Area-Berechnung | `VPIN.../src/features/va_profile.py` | kalibriert, VAH-Fehler 4,14 Punkte |
| VA-Historie 4,5 Jahre | `VPIN.../data/va/` | 55 Monatsdateien, 544.664 Zeilen |
| Ereignisstudie | `VPIN.../scripts/build_event_study.py` | 7.003 Ereignisse, austauschbare Ereignisdefinition |
| Statistik-Gerüst | `VPIN.../scripts/run_event_analysis.py` | Bootstrap, Cliff's Delta, Permutation, Störgrößen |
| Leistungsanalyse | dieser Chat, reproduzierbar | Ereigniszahl je Effektstärke |
| Topologie-Klassifikator | `GEX_Dashboard/synth_gex_test.py` | 91 % gegen synthetische Wahrheit |
| **Datenzugang NDX 2012+** | QuantConnect Cloud | **kostenlos**, Gamma + OI + IV |
| Placebo-Methodik | `GEX_Dashboard/quantconnect/09_*` | hat den einzigen Scheinbefund entlarvt |

**Alles ist auf jede andere Ereignisdefinition sofort anwendbar.**

## Fünf Fallen, die nicht wiederholt werden dürfen

1. **Zwei Preisreihen mischen.** Der April-Backtest kombinierte Sierra-Entries mit
   Parquet-Exits — konstanter Versatz von 211,50 Punkten durch die Neuadjustierung des
   back-adjusted continuous contract beim Quartals-Roll. Ergebnis war ungültig.
2. **Ohne Placebo messen.** Der Wall-Effekt sah signifikant aus, bis ein Kontrollniveau
   gleichen Abstands dasselbe zeigte.
3. **Auf geglättete Profile rechnen.** `compute_gex_profile` ist per Konstruktion ein
   starker Glätter — in der Zone Spot ±200 wird das Profil zur Geraden (r² 0,997, null
   Extrema). Die Struktur liegt auf der **Strike-Ebene** (30 Extrema, r² 0,015).
4. **Filter ohne Abstain-Zustand.** Der VPIN-Filter sagte in 87 von 87 Vergleichen
   dasselbe. Ein Filter, der nie „nein" sagt, trennt nichts.
5. **Hypothesen nach dem Ergebnis nachfassen.** Deshalb wurde der Topologie-Test in
   `VORHERSAGEN_TOPOLOGIE.md` vorab festgeschrieben und einmal geprüft.

## Was offen bleibt — und was nicht

**Nicht widerlegt**, aber ungeprüft:
- Effekte unter d ≈ 0,10 gepoolt, unter d ≈ 0,20 in Untergruppen
- Walls bei ±1 bis 3 % statt ±0,8 % — die Niveaus, über die Praktiker tatsächlich reden.
  **Die konkreteste Schwäche der bisherigen Messung.**
- Verfalls-Pinning (Ni/Pearson/Poteshman 2005) — die einzige Version mit publizierter
  Grundlage, nie getestet
- Walls als Risikoniveau statt Richtungssignal (Durchschlagswahrscheinlichkeit)
- GEX in Kombination mit Orderflow, Ordercluster, Tageszeit — also konditioniert,
  wie Praktiker es einsetzen

**Bewertung des Coordinators:** Nach vier sorgfältigen Vorab-Tests ohne Signal ist die
wahrscheinlichste Erklärung nicht, dass die richtige Variante noch fehlt. Ein fünfter
Test derselben Familie hätte geringen Erwartungswert. Die offenen Punkte oben sind
ehrlich offen — aber sie zu bearbeiten wäre eine Entscheidung gegen die bisherige
Evidenz, nicht wegen ihr.

## Empfehlung für die nächste Session

Es gibt jetzt ein **konkretes offenes Problem**, an dem sich eine neue Strategic-Runde
reiben kann — anders als vor vier Tagen, wo drei ungetestete Ideen im Regal lagen:

> Vier isolierbare, systematisch prüfbare Signale aus Optionsstruktur und Orderflow
> tragen bei NQ keinen messbaren Vorteil. Der Markt ist intraday robust mean-revertierend,
> aber die Rückkehr ist nach Kosten nicht ernte-fähig. **Was bleibt für einen Retail-Trader
> mit 5.000–10.000 €, 1–2 h/Tag und diesem Instrument?**

Alternativ: Der Cluster `aktien-retail-edge` liegt pausiert und hatte mit dem
Segment-Selektor-Axiom (A4 Coverage-Ökonomie) einen strukturell anderen Ansatz — dort
war der Engpass Datenkosten, nicht fehlende Wirkung. Die QuantConnect-Entdeckung
könnte auch dort etwas ändern.

---

## Sessions

| Datum | Slug | Status | Stärkstes Ergebnis |
|---|---|---|---|
| 2026-04-15 | 2026-04-15-futures-day-edge-strategic | COMPLETE | GTZI → GEX-Topologie → SGM als integriertes System |
| 2026-08-30 bis 09-02 | Prüfphase (kein eigener Slug) | COMPLETE | Vier Ansätze geprüft, keiner mit Signal. Infrastruktur und kostenloser Datenzugang aufgebaut. |

## Cluster-Kontext
Ausgangspunkt: Explorer-Session 2026-03-30-agentic-trading-edge (15 Hypothesen, H2 GEX-Dual-Trigger als stärkste).
Focus: Genuinen neuen Mechaniken mit strukturellem Edge finden — über bekannte Ansätze (GEX, Orderflow, Volumeprofil) hinaus.
Kernaxiom: 90%-Failure-Rate ist Populationseffekt, kein Naturgesetz. Struktureller Vorteil ist für Retail möglich.

## Offene Fäden

**Stand 2026-08-31 — Entscheidung: Umsetzung, keine neue Strategic-Session.**

Die drei Ideen aus Session 2026-04-15 (GTZI, GEX-Feld-Topologie-Karte, Strike-Gradient-Momentum)
haben alle Filter überlebt, wurden alle drei als NOVEL eingestuft — und sind **bisher nicht
umgesetzt**. Der vollständige Umsetzungsplan mit 12-Schritte-Roadmap, Abbruchpunkten,
Erfolgsschwellen und Kostenübersicht liegt in
`outputs/individual/2026-04-15-futures-day-edge-strategic/experiment-designs.md`.

**Warum dieser Cluster wieder aktiv wird:**
Die Parallel-Session `2026-08-30-aktien-retail-edge-strategic` (Cluster `aktien-retail-edge`)
hat den Aktien-Weg untersucht und ist zu einem klaren Ergebnis gekommen: Kurz- bis
mittelfristiger Einzelaktienhandel mit 5.000–10.000 € hat eine Kostenstruktur (3–4 %
Reibung pro Round-Trip, spread-dominiert), die die Bruttoerwartung fast vollständig
auffrisst — und der strukturelle Retail-Vorteil liegt ausgerechnet dort, wo die Reibung
am größten ist.

**Dieses Problem existiert bei ES/NQ-Futures nicht.** Spreads von einem Tick statt 2–3 %.
Dazu kommt vorhandene Infrastruktur: GEX-Dashboard (`gex_core.py`, `gex_intraday.py`,
`gex_sc_bridge.py`), VPIN_Regime_Detector, Sierra-Chart-Python-Pipeline,
`nq_reversion_engine.py`. Der Aufwand liegt damit in der Auswertung, nicht in der Beschaffung.

**Nächste konkrete Schritte (aus der Roadmap):**
1. Prüfen, ob `gex_core.py` bereits tägliche EOD-Snapshots persistiert. Falls nicht:
   Snapshot-Erfassung SOFORT starten — jeder Tag ohne Snapshot ist verlorene Historie.
   Diese Aktion ist zeitasymmetrisch und sollte allen anderen Entscheidungen vorausgehen.
2. Falls weniger als 90 Tage Historie vorhanden: CBOE-EOD-Backfill (Databento pay-per-use,
   0–30 USD, oder kostenlose Quellen).
3. Schritte 1–4 der Roadmap durchführen → erster Abbruchpunkt: GTZI bestätigt oder widerlegt.
   Aufwand 4–6 Tage, Kosten 0–30 USD, kein Kapitalrisiko.
4. ThetaData (25 USD/Monat) erst ab Schritt 8 — nach positivem E1/E2-Ergebnis.

**Weiterhin offen:**
- Ist Negativ-Selektion robuster gegen LLM-Fehler als Positiv-Selektion? (Coordinator-
  Hypothese CH3 aus der Aktien-Session, dort nie adressiert — hier ebenso relevant.)
- Termingeschäfte-Besteuerung: Die Verlustverrechnungsbeschränkung nach § 20 EStG für
  Termingeschäfte war Gegenstand von Gesetzgebungsverfahren. Aktueller Stand ist VOR
  Live-Trading zu verifizieren — nicht aus dem Gedächtnis annehmen.

## Bestandsaufnahme der vorhandenen Projekte — 2026-08-31

Geprüft: `/Users/rigmotion/Documents/VPIN_Regime_Detector` und `/Users/rigmotion/Documents/GEX_Dashboard`.
Zusammen rund 68.000 Zeilen Python.

**KORREKTUR 2026-08-31:** Die ursprüngliche Aussage "beide ohne Git-Versionierung" war
falsch. `VPIN_Regime_Detector/microstructure-regime-filter` ist vollständig versioniert:
109 Commits, 32 Branches, GitHub-Remote `normizen/microstructure-regime-filter`, alles
gepusht. Der Fehler entstand, weil `git log` im Elternverzeichnis ausgeführt wurde — Git
sucht aufwärts, nicht abwärts. Für `GEX_Dashboard` traf die Aussage zu — **am 2026-08-31 behoben**: `git init` durchgeführt,
Erstcommit `72cd957`, Branch `main`, 78 Dateien getrackt, .git-Verzeichnis 9 MB.
Versioniert: alle aktiven Module, `data/daily/` (33 EOD-Chain-CSVs, bei CBOE nicht
nachladbar), sowie einmalig die historischen Stände `_Scripts_earlier_versions/` und
`_GEX_Dashboard_V1/`.
Ausgeschlossen per .gitignore: `data/snapshots/` (158 MB Intraday) — **diese Daten sind
damit NICHT durch Git gesichert und ebenfalls nicht nachladbar**; separates Backup nötig.
Remote: `https://github.com/normizen/GEX_Dashboard` — Erst-Push am 2026-08-31 erfolgreich,
`main` trackt `origin/main`. (Der Push scheiterte zunächst mit HTTP 400; behoben über
`git config http.postBuffer 524288000`.)

### GEX_Dashboard — Datenlage ist der Engpass

| Was | Stand |
|---|---|
| `data/daily/` | 17 Handelstage (NDX + QQQ), 19.02.–13.03.2026 |
| `data/snapshots/` | 16 eindeutige Handelstage, gleicher Zeitraum |
| Lücke seit | 13.03.2026 — rund 5,5 Monate |
| GTZI-Bedarf | >= 90 Handelstage |

**Konsequenz:** GTZI ist mit Eigenerhebung frühestens Anfang Januar 2027 testbar
(90 Handelstage ab heute). Ein Datenprovider ist damit kein Beschleuniger, sondern die
einzige Option, GTZI in diesem Jahr zu prüfen.

**Zusätzlich:** `download_cboe.py` weist im eigenen Docstring darauf hin, dass automatisierte
Intraday-Loops gegen die CBOE-Nutzungsbedingungen verstoßen — das Script ist für den
manuellen Tagesstart-Download gebaut. Ein Cron-Job für Intraday scheidet aus. Und CBOE
liefert nur aktuelle Chains; vergangene Tage sind nachträglich nicht beziehbar.
Historie MUSS also über einen Provider kommen.

### VPIN_Regime_Detector — weiter als erinnert, mit einer weichen Stelle

`RESEARCH_STATUS.md` (Stand April 2026) dokumentiert Phase 7 als abgeschlossen:
Live-Pipeline end-to-end funktionsfähig, XGBoost V2 F1=0.737, Modell exportiert,
Sierra-Client und Regime-Server laufen. 56,2 Mio. Rows, 599.334 Dollar Bars.

Offene Schritte laut eigener Doku: `close_ffd dynamisch` -> `VA/TPO-Integration` ->
**`Strategie-Backtest`**. Letzterer ist genau die Frage "hat der Detektor Mehrwert fürs
Trading?" — sie ist im Projekt selbst als unbeantwortet markiert.

**Kritische Beobachtung (Coordinator):** Walk-Forward V2 ist mit 15/43 positiven
Sharpe-Fenstern (35 %) durchgefallen; die Doku begründet das damit, dass ein direktionaler
Return-Predictor-Test der falsche Maßstab für einen Qualitätsfilter sei. Das ist methodisch
nachvollziehbar. Aber die stattdessen bestandene Filter-Evaluation (θ=0.60, 60,5 %
verbesserte Fenster, +0.019) trägt in derselben Doku die Einschränkung, dass die Baseline
die **modell-eigene** war (−0.105) und nicht V1 (+0.035).

Damit ruht der einzige dokumentierte PASS auf einem Vergleichsmaßstab, den das Projekt
selbst als fragwürdig notiert. Das ist Dogma D11/D7 des Clusters ("Backtest-Erfolg zeigt
echten Edge an") im konkreten Fall — und es sollte vor allem Weiteren nachgerechnet werden.
Kosten: null, Daten und Modelle liegen vor.

### Nachrechnung der Filter-Evaluation — 2026-08-31

Durchgeführt, ohne Neutraining (alle Zahlen lagen als CSV vor).
Vollständige Analyse: `notes/2026-08-31-vpin-filter-reevaluation.md`.

**Ergebnis:** Der dokumentierte "Gate PASS θ=0.60" trägt nicht.
- `mean_sharpe_filt` ist bei **allen** Thresholds von 0,50 bis 0,80 negativ (bester Wert
  −0,0823 bei θ=0,50). Bei θ=0,60: −0,0855 gegen V1 +0,0353 — Differenz −0,121.
- Das Gate prüft nur `mean_improvement > 0` gegen die modell-eigene Baseline; das
  Vorzeichen des absoluten Sharpe wird nirgends geprüft.
- θ=0,60 wurde nach maximaler *Verbesserung* gewählt, nicht nach bester *Leistung*.
- Keine Transaktionskosten, kein Slippage — bei 391 Events pro Woche.
- V1 selbst ist keine gute Referenz: Median −0,0022, nur 48,8 % positive Fenster.
- **Entscheidend:** Die Filter-Evaluation leitet die Richtung aus dem Modell ab
  (`direction = np.where(p_bull > p_bear, ...)`) — exakt der Konstruktionsfehler, wegen
  dem der Walk-Forward verworfen wurde. Der bestandene Test misst dasselbe wie der
  durchgefallene.

**Einordnung — korrigiert 2026-08-31:** Der richtige Test EXISTIERT und wurde gelaufen.
`live/strategy_backtest.py` (873 Zeilen, Commits vom 20./21.04.) nimmt die Richtung aus dem
VA-Ausbruch und nutzt das Modell nur als Bestätigungsfilter — genau der Aufbau, dessen
Fehlen oben bemängelt wurde. Lauf vom 25.04.2026 (`live/logs/summary.txt`), ein Handelstag:
Win Rate Baseline 59,3 % gegen Filtered 18,2 %, P&L +5.535 USD gegen +1.875 USD,
Filtereffekt −3.660 USD.

**Aber n = 1 Tag** — statistisch bedeutungslos, keine Kosten, starke Richtungs-Schieflage
(14 von 16 Shorts weggefiltert). Der Filter ist damit weder belegt noch widerlegt.
`RESEARCH_STATUS.md` (18.04.) ist veraltet und markiert diese Arbeit fälschlich als offen.

Neuer Engpass: die Ereignis-Historie. `strategy_backtest.py` braucht `live_events.csv`
mit vah/val/poc; in `live/logs/archive/` liegt genau ein Ordner.
Details: `notes/2026-08-31-vpin-filter-reevaluation.md`, Abschnitt KORREKTUR.

## ANTWORT auf die Ausgangsfrage — 2026-08-31

**"Hat der VPIN-Regime-Filter Mehrwert fürs Trading?" — Nein, als Filter für
Value-Area-Ausbrüche nicht.**

Ereignisstudie über 4,5 Jahre (553.444 Dollar-Bars mit selbst berechneter VA,
7.003 Ereignisse), ohne jede Handelslogik. Vollständiger Bericht:
`VPIN_Regime_Detector/microstructure-regime-filter/reports/event_study/ERGEBNIS.md`

**Ebene 0 — der VA-Ausbruch selbst:** kleiner, statistisch messbarer Drift
(Median +0,75 bis +4,88 Punkte, Konfidenzintervall schließt Null aus), aber
MFE/MAE zwischen 1,00 und 1,07 und **97,5 % Reversion binnen 100 Bars**.
Fortsetzungsrate fällt von 47 % auf 32 %. Das ist Mean Reversion, kein Ausbruch.

**Ebene 1 — das Regime als Filter:** kein Effekt. Cliff's Delta bei den Renditen
zwischen −0,007 und +0,003 (Kriterium war >= 0,10), Permutations-p zwischen 0,45
und 0,92. Alle fünf Abnahmekriterien verfehlt. Die Monotonie über die
Konfidenz-Terzile ist sogar **invers**: das Terzil mit der höchsten Modellkonfidenz
hat bei kurzen Horizonten die schlechteste Rendite.

**Warum das belastbar ist:** Das Modell wurde auf exakt dem Zeitraum trainiert, den
die Studie auswertet (2021-09-13 bis 2026-03-13). Die Auswertung ist vollständig
in-sample und schmeichelt dem Modell damit systematisch. Kein Effekt in-sample
bedeutet praktisch ausgeschlossener Effekt out-of-sample.

**Was das NICHT sagt:** Nicht, dass VPIN als Konzept wertlos ist — getestet wurde ein
spezifisches Modell in einer spezifischen Anwendung. Nicht, dass andere
Ereignisdefinitionen (GEX-Level, Orderflow-Trigger) zum selben Ergebnis kämen.

**Konsequenz für den Cluster:** Weitere Arbeit an Entry-Logik, Stops oder Haltedauern
für den Ansatz "VA-Ausbruch mit Regime-Filter" wäre Optimierung auf Rauschen.
Die drei Ideen aus Session 2026-04-15 (GTZI, GEX-Topologie-Karte, SGM) sind davon
**nicht berührt** — sie setzen auf GEX-Mechanik, nicht auf den Regime-Filter.
Dieses Ergebnis schließt eine Sackgasse, es entwertet den Cluster nicht.

## Vorab-Check der drei NOVEL-Ideen — 2026-08-31

Auf 17 EOD-Chains und 87 Intraday-Snapshot-Paaren. Vollständig:
`GEX_Dashboard/PRECHECK_ERGEBNIS.md`, Commit `6b03b7d`.

**Ergebnis: positiv — aber mit einer Designkorrektur, die alles entscheidet.**

`compute_gex_profile()` glättet per Konstruktion (Black-Scholes-Gamma auf einem
hypothetischen Preis-Grid). In der Zone Spot ±200 ist das Ergebnis eine **Gerade**:
0 lokale Extrema an allen 17 Tagen, r² gegen Gerade 0,997. Auf **Strike-Ebene**
dieselbe Zone: 30 lokale Extrema, r² 0,015.

| Idee | auf geglättetem Profil | auf Strike-Ebene |
|---|---|---|
| GTZI | Persistenz 1,000 in 87/87 Intraday-Paaren (Streuung 0,002) — **tot** | Streuung 0,495, 33 % unter 0,5, 17 % negativ — **diskriminiert** |
| SGM | Gradient nahezu konstant — kein Gegenstand | Gradienten-Variabilität Median 51 — **viel Signal** |
| Topologie-Karte | 11 Dipol / 6 Monopol, aber Vortex feuert nie | neu zu definieren |

**Merksatz für Folge-Sessions:** Die GEX-Struktur liegt auf der Strike-Ebene. Jede
Glättung auf ein Preis-Grid zerstört genau das, was die drei Ideen messen wollen.
Der April-Entwurf hätte GTZI auf einem normierten Gitter implementiert — das hätte
das Signal vollständig vernichtet, ohne dass es aufgefallen wäre.

Nebenbefund: Median-Persistenz +0,726 auf Strike-Ebene zeigt, dass die Lumpigkeit
keine reine Zufallsschwankung ist — reines Rauschen läge bei null. Es gibt echte,
wiederkehrende OI-Konzentrationen.

**Zwei Probleme für die eigentliche Studie:** Bei Tagesbewegungen von 200–300 Punkten
überlappen zwei ±200-Fenster kaum (nur 12 von 16 Übergängen auswertbar) — Fenster auf
±400 bis ±500 verbreitern. Und 0DTE muss von der Strukturmessung getrennt werden;
`compute_gex` liefert die Kategorien bereits getrennt.

## Datenfrage gelöst über einen Instrumentenwechsel — 2026-08-31

**Problem:** NDX-Optionshistorie ist knapp und teuer. Cboe DataShop 900 $ (EOD) bzw.
3.000 $ (detailliert), ThetaData nur ab PRO mit ungeklärter NDX-Historie vor 2026-05-11,
EODHD führt keine Index-Optionen. Freie Quellen (optionsDX, DoltHub, Kaggle) führen
durchweg SPX, SPY, QQQ, VIX — aber kein NDX.

**Lösung: Die Methodik zuerst auf SPX/ES prüfen statt auf NDX/NQ.**

Begründung:
1. Der User handelt laut `project-context.md` **ES-mini UND NQ-mini**. SPX/ES ist damit
   kein Ersatzinstrument, sondern ein eigenes Ziel.
2. SPX ist der kanonische GEX-Markt. Wenn der Mechanismus irgendwo existiert, dann dort.
   **Scheitert er auf SPX mit reichlich Daten, rettet ihn NDX nicht.**
3. optionsDX bietet SPX-Ketten 2010–2023, EOD bis minütlich, Preisspanne 0–50 $,
   mit Greeks, IV, Bid/Ask und Underlying-Kurs. 2022–2023 deckt die frühe 0DTE-Phase ab
   (SPX hatte ab 2022 tägliche Verfalltermine).
4. ES-Futures-Bars kann der User selbst aus Sierra Chart exportieren — dieselbe Prozedur
   wie seinerzeit für NQ, Pipeline vorhanden (`scripts/import_sierra_csv.py`,
   `build_dollar_bars.py`). Kostenlos.

**Gesamtkosten des Machbarkeitstests: 0 bis 50 $.**

**Vor dem Download zu prüfen:** Die optionsDX-Feldbeschreibung nennt Greeks, IV,
Bid/Ask/Last und Underlying — **Open Interest wird nicht ausdrücklich genannt**.
Ohne OI ist kein GEX rechenbar. Das ist der erste zu klärende Punkt.

**Grenze der Übertragbarkeit:** Ein positives Ergebnis auf SPX/ES überträgt sich nicht
automatisch auf NDX/NQ — andere Marktstruktur, anderer Teilnehmermix, andere
Strike-Dichte. Es rechtfertigt aber dann den NDX-Datenkauf, der bis dahin auf Hoffnung
beruhen würde.

## GEX-Wall-Hypothese: negativer Befund — 2026-08-31

Ereignisstudie über **1.409 Handelstage (2021–2026)** auf QuantConnect-Daten
(NDXP, Gamma und Open Interest, kostenlos in der Cloud). Skripte:
`GEX_Dashboard/quantconnect/`.

**Der entscheidende Test — Placebo-Kontrolle:**

| h | Median Wall | Median Placebo | Cliff d | p |
|---|---|---|---|---|
| 15 | −1,80 | +0,61 | −0,025 | 0,28 |
| 30 | −5,44 | −3,12 | −0,019 | 0,39 |
| 60 | −0,94 | +0,68 | −0,004 | 0,50 |
| 120 | −5,14 | −1,94 | −0,009 | 0,40 |

n = 1.430 Wall gegen 1.459 Placebo. Das Kontrollniveau war ein Korb mit
**niedrigem** GEX in ähnlichem Abstand auf derselben Seite.

**Der GEX-Wall ist von einem beliebigen Kursniveau gleichen Abstands nicht
unterscheidbar.** Die in Zelle 08 gemessene Abweisung (MFE/MAE 0,89, Median-Rendite
negativ) war **allgemeine Mean Reversion**, kein Wall-Effekt. Ohne die
Placebo-Kontrolle wäre sie als Befund durchgegangen.

**Regime-Konditionierung (vom User angeregt): ebenfalls kein Signal.**
Netto-GEX über die gesamte Kette, positiv an 65 % der Tage — gute Variation.
Aber: gepoolt Cliff's d <= 0,045, Call-Wall nach Regime <= 0,047,
Put-Wall nach Regime <= 0,073. Alle p über 0,09.

**Nebenbefund:** Netto-GEX-Vorzeichen stimmt bei ±2 % zu 97 %, bei ±5 % zu 98 %
mit der Gesamtkette überein. Ein enges Fenster reicht — relevant für ein
späteres Live-System.

### Was widerlegt ist und was nicht

**Widerlegt (ausreichend ausgestattet):** Ein Effekt des Wall-Kontakts über
generische Mean Reversion hinaus, mit d >= 0,10. Bei n = 2.889 gut messbar,
gemessen wurde d < 0,03.

**Nicht widerlegt:** Effekte unter d ≈ 0,10 gepoolt und unter d ≈ 0,20 in den
Regime-Untergruppen (n = 260 bis 464). Andere Wall-Definitionen. Intraday
aktualisiertes GEX statt EOD vom Vortagesschluss. Andere Ereignisdefinitionen.

### Einordnung

Damit sind **zwei** Filterideen dieses Clusters am selben Muster gescheitert:
der VPIN-Regime-Filter und die GEX-Wall-Mechanik. Beide zeigten in der
gepoolten Rohmessung etwas, das nach Kontrolle verschwand.

Die drei NOVEL-Ideen aus 2026-04-15 sind davon unterschiedlich betroffen:
- **GTZI** — misst Persistenz, funktioniert als Messgröße (Streuung 0,26,
  12 % unter 0,5), aber die Ereignisrate ist mit 0,08/Tag zu niedrig
- **Topologie-Karte** — Klassifikation funktioniert (91 % gegen synthetische
  Wahrheit), aber sie unterscheidet keine Kursverläufe
- **SGM** — als Wall-Gradient operationalisiert und hier mitgetestet: kein Signal

**Die Infrastruktur bleibt.** VA-Berechnung, Ereignisstudie, Leistungsanalyse,
Placebo-Methodik und ein kostenloser Datenzugang über 14 Jahre sind für jede
weitere Ereignisdefinition sofort einsetzbar.


## Topologie-Test: negativer Befund — 2026-09-02

Vorhersagen vorab festgeschrieben in `GEX_Dashboard/quantconnect/VORHERSAGEN_TOPOLOGIE.md`
(Commit `064786b`), getestet mit `10_topologie_test.py` (Commit `2637e63`).
1.387 Handelstage 2021–2026.

**Typverteilung — der Klassifikator trennt tatsächlich:**
Dipol 792 (56,5 %) · Monopol 436 (31,1 %) · Vortex 174 (12,4 %). Keine Entartung zu
89 % Dipol wie im synthetischen Nulltest befürchtet, alle drei über der 150er-Schwelle.

| Messgröße | Monopol | Dipol | Vortex | Vorhersage |
|---|---|---|---|---|
| Varianzverhältnis | 0,888 | 0,861 | **0,914** | Vortex am höchsten — **erfüllt** |
| Effizienzquotient | 0,123 | 0,117 | **0,128** | Vortex am höchsten — **erfüllt** |
| Kreuzungen | 0,003 | 0,003 | 0,005 | Dipol > Monopol — **verfehlt** |
| Range % | 1,33 | 1,36 | **1,29** | Vortex > Monopol — **verfehlt, Gegenrichtung** |

**2 von 4 Vorhersagen.** Unter der Nullhypothese wären 1,67 Treffer zu erwarten.

**Effektstärken praktisch null:** Cliff's d zwischen −0,004 und +0,051, Kriterium war 0,10.

**Abnahme:** Kriterium 1 erfüllt, Kriterien 2, 3 und 4 verfehlt. Laut Vorabfestlegung
zählt „drei von vier" bereits als negativ — hier ist es eins von vier.

**Bemerkenswert:** Die beiden Trending-Vorhersagen trafen *beide* und in dieselbe
Richtung. Vortex ist auf beiden Maßen der trendigste Typ, wie „Kompression → Breakout"
behauptet. Nur ist der Unterschied mit d ≈ 0,05 bedeutungslos. Die Range-Vorhersage ging
sogar in die Gegenrichtung — Vortex-Tage haben die kleinste Range.

**Und ein Befund über alle Gruppen hinweg:** Alle Varianzverhältnisse liegen zwischen
0,86 und 0,91, also deutlich unter dem Zufallslauf-Wert von 1,0. NDX kehrt intraday
zurück, unabhängig von der GEX-Struktur — die dritte unabhängige Bestätigung desselben
Bildes.
