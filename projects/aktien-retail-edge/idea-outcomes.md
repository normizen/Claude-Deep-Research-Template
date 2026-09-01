# Idea-Outcomes — aktien-retail-edge

Dokumentiert, was mit Ideen aus dem Strategic-Innovation-Prozess passiert ist —
sowohl Eliminiertes (damit es nicht erneut generiert wird) als auch Überlebendes.

---

## Session 2026-08-30-aktien-retail-edge-strategic — Durchlauf 1

**Seed-Domänen:** Perkolationstheorie (1) + Quorum Sensing (7)
**Ergebnis: 0 von 8 Ideen überlebt Phase 4.**

### Gemeinsame Wurzelursache — WICHTIG für Folge-Sessions

Alle acht Ideen brauchten entweder (a) laufend aktualisierte Netzwerktopologie-Daten
(Analystencoverage, institutionelle Halterstrukturen, Lieferketten-Nachbarschaften) oder
(b) verlässliche Klassifikation der Order-Herkunft. Beides ist für einen deutschen
Retail-Trader mit IBKR-Zugang und moderatem Budget nicht existent, institutionell teuer
oder prinzipiell fehlkalibriert.

**Lehre für die Domänen-Auswahl:** Perkolationstheorie und Quorum Sensing sind beide
*netzwerktopologie-hungrige* Domänen. Ihre Kernprinzipien lassen sich ohne Kenntnis der
Netzwerkstruktur nicht operationalisieren. Bei einem Retail-Constraint müssen Seed-Domänen
danach mitgewählt werden, ob ihr Kernprinzip auf **beobachtbaren** Daten abbildbar ist.
Die Kombination beider netzwerklastiger Domänen war ein Seeding-Fehler, kein Ideenfehler.

### Eliminierte Ideen

| ID | Titel | Kriterium | Tötender Einwand |
|---|---|---|---|
| ID1 | Perkolations-Coverage-Radar | Datenzugang | Coverage-Kipppunkt-Nähe ist ex ante nicht beobachtbar; verfügbare Proxies sind gewöhnliches Momentum, keine echte Netzwerkinformation |
| ID2 | Small-Lot-Quorum-Detektor | Unmöglich | Ordergröße ist kein verlässlicher Retail-Indikator — institutionelle Algos zerlegen Orders bewusst in retail-große Häppchen. Konzeptioneller Fehler, kein Datenproblem |
| ID3 | Doppel-Gate Perkolation+Quorum | Datenzugang | Erbt beide Fehler von ID1 und ID2, zusätzlich zu niedrige Trade-Frequenz |
| ID4 | Perkolations-Sizing | **Axiom-Verstoß** | Vermischt Marktwirkungsrisiko (A5) mit Gap-Risiko (A7); die Positionsgröße wächst genau dann, wenn auch die Gap-Wahrscheinlichkeit steigt |
| ID5 | Sektor-Perkolationscluster | Datenzugang / Eingepreist | "Nachbarschaft" ist ein institutionelles Datenprodukt; die kostenlose Alternative (Sektor-Zugehörigkeit) ist seit 2008 akademisch dokumentiert und längst eingepreist |
| ID6 | Quorum-Divergenz am Perkolationsrand | Datenzugang | Kombiniert zwei je einzeln schon grenzwertige, dünn besetzte Datenquellen |
| ID7 | Asynchroner Wochen-Takt | Nicht strukturell neu | Reine Standard-Swing-Trading-Praxis, kein eigener Signalmechanismus; delegiert Gap-Schutz an das bereits eliminierte ID4 |
| ID8 | Anti-Diversifikation über Trigger-Typ | Liquidität | Konzentriert 2–4 Positionen exakt im illiquiden Small-Cap-Zielsegment ohne Exit-Mechanismus; ein erzwungener Stop-Exit löst dort selbst den Marktwirkungseffekt aus, den die Strategie vermeiden will |

### Was auch die besten dieser Ideen nicht geliefert hätten

- Keine hätte echten Vorlauf **vor** der Marktentfaltung geliefert — bestenfalls "früher als
  der breite Markt", nicht "vor der Entfaltung"
- Keine garantiert eigenständig die harte Risikogrenze
- Keine löst das 1–2 h/Tag-Zeitbudget wirklich: die laufende Datenpflege hätte deutlich mehr
  Aufwand verlangt als wöchentliches Signal-Ablesen

### Empfehlung des Advocatus für den nächsten Durchlauf

Neue Ideengenerierung aus retail-zugänglicheren Mechanismen — oder explizite Prüfung
gröberer, aber tatsächlich beobachtbarer Proxies (Marktkapitalisierungs- und Volumen-
Momentum, quartalsverzögerte 13F-Filings, Stimmrechtsmitteilungen nach WpHG).

---

## Session 2026-08-30-aktien-retail-edge-strategic — Durchlauf 2

**Seed-Domänen:** Predictive Coding (13) + Signaling-Theorie (25)
**Ergebnis: 2 von 10 Ideen überleben Phase 4.**

Durchlauf 2 wurde nötig, weil Durchlauf 1 vollständig an Datenzugang scheiterte. Neuer,
verpflichtender Beobachtbarkeits-Filter in Phase 2b und 3b: Jede Domäne und jede Idee muss
ihre konkret beschaffbare Datenquelle benennen. Zusätzlich musste jede Idee begründen,
warum ihr Effekt im Zielsegment nicht eingepreist ist.

### Eliminierte Ideen

| ID | Titel | Kriterium | Tötender Einwand |
|---|---|---|---|
| ID10 | Eigen-Trend-Baseline | Eingepreist | Im Kern die klassische SUE-/Seasonal-Random-Walk-Baseline aus der PEAD-Literatur der 1980er — kein neues Konstrukt |
| ID11 | Guidance-Spezifitäts-Drift | Datenzugang | Stützt sich auf Call-Transkripte, die für die meisten deutschen Small-/Midcaps ohne Coverage nicht existieren |
| ID12 | CapEx-Spezifitäts-Filter | Arbeitsaufwand | Klassifikation erfordert Lesen von Geschäftsbericht-Anhang-Fließtext pro Kandidat und Jahr — exakt die manuelle Fundamentalarbeit, die der User nicht leisten kann oder will |
| ID14 | Rückkauf-Exekutions-Lücke | Eingepreist | Repurchase-Completion-Rate als Renditeprädiktor ist seit Stephens & Weisbach 1998 dokumentiert; A4 trägt nicht, weil die Berechnung triviale Bilanzarithmetik wäre |
| ID15 | Divergenz-Signal | Eingepreist + Frequenz | Erbt das eingepreiste Fundament von ID10, zusätzlich Frequenzproblem durch Doppelbedingung |
| ID16 | Peer + Insider AND-Gate | Kosten/Steuer | Konjunktion zweier seltener Signale erzeugt zu wenige Trades pro Jahr für Relevanz nach Kosten und Steuer |
| ID17 | Aufmerksamkeitsarchitektur | Nicht eigenständig | Kein eigenes Marktsignal, sondern parasitäre Filterschicht über andere Ideen — nicht eigenständig prüfbar |
| ID18 | Guidance-Trefferquote | Zielkonflikt | Funktioniert am schlechtesten genau bei jungen Firmen, die dem Kernziel "vor der Entfaltung" am nächsten stehen |

### Überlebende Ideen

#### ID9: Peer-Cluster-Synthetischer-Konsens
**Kern-Idee:** Wo für einen Small Cap kein Analystenkonsens existiert, wird er selbst konstruiert — der Guidance-Median einer selbst gebauten Peer-Gruppe dient als Erwartungswert, gegen den die Überraschung gemessen wird.
**Seed-Domänen:** Predictive Coding (Vorhersagefehler als Signal) + Signaling-Theorie
**Phase 4:** ÜBERLEBT — Advocatus-Konfidenz Mittel
**Warum:** Reale, zugängliche Datenquellen (DGAP-Ad-hocs, Bundesanzeiger); das A4-Argument trägt tatsächlich, weil im unterversorgten Segment der einpreisende Mechanismus fehlt.
**Stärkster verbleibender Einwand:** Subjektive und kleine Peer-Gruppe als Rauschquelle; Exit-Realität im illiquiden Segment ungeklärt.
**Novelty-Check:** **NOVEL** — keine akademischen Papers, kommerziellen Screener oder Literaturquellen beschreiben die spezifische Konstruktion "Peer-Median-Guidance als Ersatz für fehlenden Analystenkonsens". Peer-Benchmarking existiert allgemein; die titel-spezifische Konstruktion für coverage-freie Werte ist nicht standardisiert. Offene Frage ist nicht Novelty, sondern Machbarkeit (Peer-Auswahl, konsistente Verdichtung von Fließtext über Quartale).

#### ID13: Insider-Kauf-Personen-Baseline
**Kern-Idee:** Die Signalstärke eines Insiderkaufs bemisst sich nicht am Absolutbetrag, sondern relativ zum bisherigen Handelsmuster der konkreten Person — ein Vorstand, der nie kauft und plötzlich kauft, sagt mehr als einer, der routinemäßig zukauft.
**Seed-Domänen:** Signaling-Theorie (kostspieliges Signal)
**Phase 4:** ÜBERLEBT — Advocatus-Konfidenz Hoch
**Warum:** Strukturierte, reale BaFin-Daten (Directors' Dealings), gut automatisierbar, passt ins 1–2-h-Zeitbudget.
**Stärkster verbleibender Einwand:** Dünne Handelshistorie vieler Insider bei Small Caps macht die persönliche Baseline statistisch wacklig; Exit-Realität ungeklärt.
**Novelty-Check:** **ÄHNLICHES EXISTIERT** — Cohen, Malloy & Pomorski (2012, Journal of Finance) definieren "Routine vs. Opportunistic Insider Trading", exakt die Kernmechanik von ID13. Befund dort: Routine-Insider erzeugen naeherungsweise null Abnormal Return, opportunistische rund 82 Basispunkte pro Monat. Die strukturelle Idee ist nicht neu; neu waere allenfalls die Implementierung auf BaFin-Directors'-Dealings im deutschen Small-Cap-Kontext.
**Bewertung des Coordinators:** Kein Ausschlussgrund. Fuer den Zweck dieser Session — eigenes Kapital, nicht Publikation — ist eine extern validierte Mechanik mit dokumentierter Effektgroesse wertvoller als eine neue, unvalidierte. Aber die Herkunft muss offengelegt bleiben.

### Kombinierbarkeit

ID9 und ID13 sind strukturell unabhängig und ergänzbar, aber **nicht** als striktes AND-Gate —
das war ID16 und wurde wegen zu geringer Signalfrequenz eliminiert. Tragfähiger Ansatz für
Phase 6/7: ID13 als **weicher Konfidenz-Booster** auf ID9-Kandidaten, ohne starres Zeitfenster,
damit die Basisfrequenz von ID9 nicht künstlich weiter sinkt.

### Was auch die Überlebenden nicht können

- Beide erkennen die Diskrepanz **erst im Moment des öffentlichen Bekanntwerdens**, nicht
  wirklich davor. Der ursprüngliche Wunsch "vor der Entfaltung" wird nur teilweise erfüllt.
- Keine garantiert eigenständig die harte Risikogrenze — das bleibt Aufgabe des Positionssizing.
- Keine löst das Exit-Problem im illiquiden Small-Cap-Segment.
- Beide liefern vermutlich moderate, nicht hohe Trade-Frequenz. Profitmaximierung bleibt
  ein Baustein, kein vollständiges System.
