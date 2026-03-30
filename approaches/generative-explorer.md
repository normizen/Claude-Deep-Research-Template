# Generative Explorer

## Metadaten

- **Name:** Generative Explorer
- **Am besten für:** Themen bei denen das Ziel nicht ist zu dokumentieren was existiert, sondern neue Möglichkeiten zu entdecken, Hypothesen zu entwickeln und konkrete Experimente / Implementierungsideen zu generieren — besonders in schnell bewegenden Feldern
- **Domänen:** 2–6+ (flexibel)
- **Stakes:** Variabel — Exploration-Orientierung, nicht Entscheidungs-Grundlage
- **Sub-Agenten:** Ja (echte Claude Code Sub-Agenten via Agent-Tool)
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

- User fragt explizit nach neuen Möglichkeiten, Ideen, kreativen Kombinationen
- Thema bewegt sich schnell — etablierte Literatur ist veraltet oder dünn
- Ziel ist: "Was können wir jetzt bauen/testen?" statt "Was wurde schon bewiesen?"
- Explorer-Modus gewünscht: spekulative Ansätze sind willkommen wenn als solche gekennzeichnet
- Multi-Agent soll nicht nur recherchieren sondern Hypothesen erzeugen und Experimente designen

**Nicht verwenden wenn:**
- Hauptziel ist verlässliche Faktenbasis für Hochrisiko-Entscheidungen → Multi-Agent Adversarial
- Thema ist klar abgegrenzt und gut dokumentiert → Single-Agent Deep Dive
- Synthese bekannter Literatur reicht aus → Cross-Domain Synthesis

## Der Kernunterschied zu anderen Ansätzen

Cross-Domain Synthesis fragt: *"Was sagen diese Domänen über das Thema?"*
Generative Explorer fragt: *"Was ist noch nicht gesagt worden — und was können wir damit bauen?"*

Der Unterschied liegt in der Richtung: Synthesis schaut zurück auf vorhandenes Wissen.
Explorer schaut vorwärts auf das was möglich ist. Beide Phasen existieren — aber Explorer hat
explizit eine Hypothesen-Generierungs- und Experiment-Design-Phase die in anderen Ansätzen fehlt.

## Selbst-Check

Vor der Ausführung prüfen:
1. Ist das Ziel tatsächlich generativ — neue Möglichkeiten entdecken, nicht nur dokumentieren?
2. Ist der User bereit mit spekulativen und ungeprüften Hypothesen zu arbeiten?
3. Sind aktuelle Web-Quellen (letzte 6 Monate) wichtiger als klassische Literatur?

Falls alle drei "ja": Generative Explorer ist richtig.
Falls nur 1+2 aber nicht 3: Cross-Domain Synthesis mit explizitem "Emergente Ideen"-Auftrag.

## Rollen und Modell-Zuweisungen

| Rolle | Modell | Aufgabe |
|---|---|---|
| Research Coordinator | claude-sonnet-4-6 | Orchestrierung, Hypothesen-Seeding, finale Überprüfung |
| Web Researcher (Recency-Fokus) | claude-haiku-4-5-20251001 | Quellen letzte 6 Monate bevorzugt, aktuelle Frameworks/Repos/Practitioners |
| Domain Researcher [pro Domäne] | claude-sonnet-4-6 | Domänenrecherche + explizit: Lücken und Chancen identifizieren |
| Hypothesis Generator | claude-sonnet-4-6 | Generiert neue Hypothesen aus Domänen-Findings — ohne Beweispflicht |
| Experiment Designer | claude-sonnet-4-6 | Macht Hypothesen konkret: Was ist jetzt baubar? Wie testen? |
| Formatter | claude-haiku-4-5-20251001 | Finales Dokument-Assembly |

**Hinweis zum Hypothesis Generator:**
Dieser Agent arbeitet *nach* den Domain Researchers aber *vor* dem Experiment Designer.
Er ist explizit ermutigt spekulativ zu sein — sein Output wird von Experiment Designer
auf Umsetzbarkeit geprüft. Hypothesen müssen in den Domänen-Findings verwurzelt sein,
dürfen aber über sie hinausgehen.

## Orchestrierungs-Sequenz

### Schritt 0: Coordinator — Hypothesen-Seeding

Bevor Agenten gespawnt werden:
1. Lese `context/from-human/[SLUG]/project-context.md`
2. Formuliere 3–5 Ausgangs-Hypothesen aus eigener Einschätzung:
   - Was wäre besonders wertvoll zu entdecken?
   - Welche Verbindungen klingen vielversprechend?
   - Was fehlt in der bekannten Literatur wahrscheinlich?
3. Schreibe diese in `scratchpad/[SLUG]-coordinator-hypotheses.md`
4. Diese Hypothesen sind NICHT für Domain Researchers — nur für späteren Vergleich

### Schritt 1: Web Researcher — Recency-Fokus (Haiku)

**Zeitpunkt:** Früh — Quellen für alle Domänen sammeln

**Besondere Instruktionen für diesen Ansatz:**

Dieser Approach kennt zwei Recency-Modi — welcher gilt steht im `project-context.md`:

**Modus A — Recency-Weighted (Default):**
- Neuere Quellen (<6 Monate) bevorzugen, aber ältere einbeziehen wenn relevant
- Kein Ausschluss — nur Priorisierung
- Datum jeder Quelle ist Pflichtfeld

**Modus B — Recency-Strong (wenn User "nur letzte 6 Monate" oder ähnliches sagt):**
- Mindestens 80% der Quellen müssen <6 Monate alt sein
- Ältere Quellen nur mit explizitem `[OLDER-FOUNDATION]`-Tag — und einer Pflichtbegründung in 1 Satz: warum ist diese Quelle trotz Alter noch relevant?
- Kein echter Hard-Cut: eine Quelle die das Fundament aller neuen Entwicklungen ist bleibt drin — aber sie muss begründet werden
- Datum jeder Quelle ist Pflichtfeld

**Gilt für beide Modi:**
- GitHub-Repos, Practitioners-Blogs, Substack, arXiv Preprints explizit einschließen
- Auch "wenige aktuelle Papers gefunden" ist valides Ergebnis → zeigt Frontier-Charakter
- Bei AI/Tech-Themen: Modell-Versionen und Framework-Versionen in Quellen notieren

**Zusatz-Tag:**
- `[FRONTIER]` — Quelle beschreibt etwas das noch kein Peer-Review hatte aber von Practitioners aktiv genutzt wird
- `[OLDER-FOUNDATION]` — Quelle ist älter als 6 Monate, wird aber einbezogen weil sie das Fundament aktueller Entwicklungen bildet (nur in Modus B mit Pflichtbegründung)

### Schritt 2: Domain Research (Sonnet — sequenziell)

Für JEDE Domäne einen eigenen Domain Researcher spawnen.
Zusätzlich zu den Standard-Sektionen (aus cross-domain-synthesis.md) muss jeder
Domain Researcher eine verpflichtende **Explorer-Sektion** liefern:

```
## Explorer-Sektion

### Identifizierte Lücken
[Was existiert NICHT in dieser Domäne, obwohl es sinnvoll wäre?
Konkret: "Es gibt keine Studie zu X + Y obwohl beide Komponenten separat belegt sind."]

### Frontier-Beobachtungen
[Was passiert gerade in dieser Domäne — GitHub-Aktivität, neue Frameworks,
Practitioners-Experimente — das noch keine akademische Aufarbeitung hat?]

### Hypothesen aus dieser Domäne
[Was würde diese Domäne vorhersagen wenn man sie mit anderen kombiniert?
Spekulativ ist OK — als solches kennzeichnen.]

### Was wäre jetzt baubar?
[Welche konkreten Experimente oder Implementierungen wären mit verfügbaren
Tools möglich? Minimale Anforderungen nennen.]
```

### Schritt 3: Hypothesis Generator (Sonnet)

**Zeitpunkt:** Nach ALLEN Domain Researchers

**Liest:** Alle Domänen-Findings — insbesondere die Explorer-Sektionen

**Aufgabe:**
Generiere einen strukturierten Katalog neuer Hypothesen. Jede Hypothese muss:
- In mindestens einem Domänen-Finding verwurzelt sein
- Eine testbare Vorhersage enthalten
- Eine Einschätzung der Plausibilität haben (nicht Beweis — Plausibilität)
- Einen ersten Gedanken haben wie man sie testen würde

Explizit: Hypothesen DÜRFEN über die Domänen-Findings hinausgehen.
"Stark spekulativ aber konzeptionell vielversprechend" ist ein valider Output.

**Output:** `outputs/individual/[SLUG]/hypothesis-catalogue.md`

### Schritt 4: Experiment Designer (Sonnet)

**Zeitpunkt:** Nach Hypothesis Generator

**Liest:**
- Alle Domänen-Findings
- `hypothesis-catalogue.md`
- `context/from-human/[SLUG]/project-context.md` (Hardware, Budget, Constraints)

**Aufgabe:**
Für die vielversprechendsten Hypothesen (Top 5–8): konkrete Experiment-Designs.

Pro Experiment:
- **Hypothese:** [Was wird getestet?]
- **Methode:** [Wie konkret — Code, Backtest, A/B-Test, manuelle Analyse?]
- **Tools/Stack:** [Exakt welche Tools, Libraries, Datenzugänge]
- **Aufwand:** [Stunden/Tage für Minimal-Version]
- **Erfolgskriterium:** [Woran erkennt man ob die Hypothese zutrifft?]
- **Failure Mode:** [Was würde das Experiment ungültig machen?]
- **Claude Code Rolle:** [Wie kann Claude Code dieses Experiment unterstützen/automatisieren?]
- **Nächster konkreter Schritt:** [Erste Aktion um anzufangen — klein und spezifisch]

**Output:** `outputs/individual/[SLUG]/experiment-designs.md`

### Schritt 5: Coordinator Review

1. Vergleiche Coordinator-Hypothesen (Schritt 0) mit generierten Hypothesen
2. Notiere Übereinstimmungen und Überraschungen in Scratchpad
3. Wähle Top-3-Experimente für prominente Platzierung im Final Report
4. Prüfe ob Steuer/Regulatorische Constraints berücksichtigt wurden (falls relevant)

### Schritt 6: Formatter (Haiku)

Erstelle Final Report mit Explorer-spezifischer Struktur (siehe Output-Struktur unten).

---

## Sub-Agent Invocations

### AGENT SPAWN: Web Researcher (Recency-Fokus)

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 1

**Prompt-Template:**

```
Du bist Web Researcher für ein Generative-Explorer-Projekt.

Lese: context/from-human/[SLUG]/project-context.md

Domänen: [COORDINATOR FÜLLT EIN]

Deine Aufgabe:
Sammle Quellen. Datum jeder Quelle ist Pflichtfeld.

Prüfe zuerst `project-context.md` auf den Recency-Modus:

**Modus A (Default — kein expliziter Hinweis im project-context.md):**
Neuere Quellen bevorzugen, ältere einbeziehen wenn relevant. Kein Ausschluss.

**Modus B ("nur letzte 6 Monate" oder ähnlich im project-context.md):**
Mindestens 80% der Quellen <6 Monate. Ältere Quellen nur mit:
- Tag: `[OLDER-FOUNDATION]`
- Pflichtbegründung (1 Satz): warum ist diese Quelle trotz Alter noch relevant?

Spezielle Tags:
- [FRONTIER] — Practitioners-Erfahrung ohne Peer-Review aber aktiv genutzt
- [LAB-ENVIRONMENT] — Nur simulierte Umgebungen
- [COMMERCIAL-BIAS] — Produkt/Tool-Werbung
- [OUTDATED] — Älter als 12 Monate bei schnell bewegenden Themen

Für jede Domäne: Minimum 3 Quellen. Falls weniger als 3 aktuelle Quellen gefunden:
Explizit notieren → "Frontier-Bereich, wenig Dokumentation" ist ein valides Ergebnis.

Speichere als: context/from-internet/sources-[DATUM].md

Format pro Quelle:
### [Titel]
- URL: [url]
- Datum: [YYYY-MM]
- Tag: [FRONTIER / LAB-ENVIRONMENT / COMMERCIAL-BIAS / OUTDATED / kein Tag]
- Zusammenfassung: [2-3 Sätze]
- Warum relevant für Explorer-Ziel: [1 Satz]
```

---

### AGENT SPAWN: Domain Researcher

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 2 — sequenziell pro Domäne

**Prompt-Template:** Wie in `cross-domain-synthesis.md`, PLUS die Explorer-Sektion
am Ende jedes Findings-Dokuments (siehe Schritt 2 oben).

---

### AGENT SPAWN: Hypothesis Generator

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 3

**Prompt-Template:**

```
Du bist Hypothesis Generator für ein Generative-Explorer-Projekt.

Übergeordnetes Thema: [COORDINATOR FÜLLT EIN]
Domänen: [COORDINATOR FÜLLT EIN]

Lese ALLE Domänen-Findings — insbesondere die Explorer-Sektionen:
[COORDINATOR FÜLLT EIN: Liste aller Findings-Dateien]

Deine Aufgabe:
Generiere einen Hypothesen-Katalog. Qualität > Quantität — 5 starke Hypothesen
sind besser als 15 schwache.

Was eine gute Hypothese ist:
1. Sie entsteht aus der KOMBINATION von ≥2 Domänen (nicht aus einer Domäne allein)
2. Sie macht eine testbare Vorhersage
3. Sie ist nicht offensichtlich — kein Single-Domain-Researcher hätte sie allein formuliert
4. Sie zeigt auf eine Lücke oder Chance die bisher nicht adressiert wurde

Hypothesen-Typen (alle willkommen):
- MECHANISTISCH: "X funktioniert weil Y aus Domäne A den Mechanismus Z aus Domäne B verstärkt"
- METHODISCH: "Methode A aus Domäne X würde Problem B in Domäne Y lösen"
- ARCHITEKTONISCH: "Wenn System A und System B so kombiniert werden, entsteht Eigenschaft C"
- FRONTIER: "Aktuelle Technologie T macht Ansatz A erstmals praktikabel obwohl er theoretisch seit Jahren bekannt ist"

Format für jede Hypothese:

### H[N]: [Kurztitel]

**Typ:** [Mechanistisch / Methodisch / Architektonisch / Frontier]
**Domänen:** [A] + [B] → [emergente Verbindung]
**Hypothese:** [Präzise Formulierung — was wird behauptet?]
**Testbare Vorhersage:** [Was müsste man beobachten wenn die Hypothese stimmt?]
**Verwurzelung in Findings:** [Welche konkreten Findings stützen das?]
**Plausibilität:** [Hoch / Mittel / Niedrig / Spekulativ — mit Begründung]
**Warum noch nicht untersucht:** [Was hat die Erforschung bisher verhindert?]
**Erste Test-Idee:** [Minimalster Weg diese Hypothese zu prüfen]

Speichere als: outputs/individual/[SLUG]/hypothesis-catalogue.md
```

---

### AGENT SPAWN: Experiment Designer

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 4

**Prompt-Template:**

```
Du bist Experiment Designer für ein Generative-Explorer-Projekt.

Übergeordnetes Thema: [COORDINATOR FÜLLT EIN]

Lese:
- outputs/individual/[SLUG]/hypothesis-catalogue.md
- context/from-human/[SLUG]/project-context.md (Hardware, Budget, Constraints)
- Alle Domänen-Findings (Explorer-Sektionen)

Deine Aufgabe:
Wähle die 5–8 vielversprechendsten Hypothesen aus dem Katalog und designe
für jede ein konkretes, umsetzbares Experiment.

Priorisierungs-Kriterien:
1. Plausibilität (Hoch > Mittel > Spekulativ)
2. Retail-Umsetzbarkeit (mit verfügbaren Tools, kein institutioneller Zugang nötig)
3. Aufwand/Nutzen-Verhältnis (Minimal-Test möglich?)
4. Neuheit (entsteht wirklich etwas Neues daraus?)

Format pro Experiment:

### E[N]: [Titel — direkt aus H[N]]

**Bezug:** Hypothese H[N]
**Hypothese (Kurzform):** [1 Satz]

**Methode:**
[Konkrete Beschreibung — kein Buzzword-Padding.
Was genau wird gemacht, in welcher Reihenfolge?]

**Benötigter Stack:**
- Tools: [exakte Namen und Versionen wenn relevant]
- Datenzugänge: [welche APIs/Datasets, Kosten]
- Hardware: [läuft das auf [USER-HARDWARE aus project-context.md]?]
- Kosten: [geschätzt — einmalig und laufend]

**Zeitaufwand (Minimal-Version):**
[Stunden oder Tage für erste lauffähige Version]

**Claude Code Rolle:**
[Wie kann Claude Code konkret helfen — Code schreiben, Backtest orchestrieren,
Daten analysieren, iterieren? Spezifisch, nicht generisch.]

**Erfolgskriterium:**
[Woran erkennt man ob die Hypothese bestätigt / widerlegt / unklar ist?
Messbare Schwellenwerte wenn möglich.]

**Failure Modes:**
- [Was könnte das Experiment ungültig machen?]
- [Welche Annahmen können brechen?]

**Nächster konkreter Schritt:**
[Eine einzige Aktion, klein und spezifisch, die man morgen starten könnte]

**Konfidenz:** [Hoch / Mittel / Niedrig / Spekulativ]

Speichere als: outputs/individual/[SLUG]/experiment-designs.md
```

---

### AGENT SPAWN: Formatter

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 6

Speichere Final Report als:
`outputs/aggregated/mk-combined/[DATUM]-[SLUG]-explorer-report.md`

---

## Output-Struktur

```
outputs/
├── individual/
│   ├── [domäne-a]/
│   │   └── YYYY-MM-DD-[domäne-a]-findings.md     # + Explorer-Sektion
│   ├── [domäne-b]/
│   │   └── YYYY-MM-DD-[domäne-b]-findings.md
│   └── [SLUG]/
│       ├── hypothesis-catalogue.md
│       └── experiment-designs.md
└── aggregated/
    └── mk-combined/
        └── YYYY-MM-DD-[slug]-explorer-report.md

scratchpad/
└── [SLUG]-coordinator-hypotheses.md               # Coordinator Pre-Research Hypothesen

context/
└── from-internet/sources-[DATUM].md              # Recency-Fokus
```

## Final Report Struktur (Explorer-spezifisch)

```markdown
# [Thema] — Explorer Report

## Executive Summary
[Was wurde entdeckt? Welche Hypothesen sind am stärksten?
Welches Experiment hat die höchste Priorität? Ehrlich über Konfidenz.]

## Top-Experimente (priorisiert)

### #1 — [Experiment-Titel]
[Vollständig aus experiment-designs.md]

[Weitere Experimente...]

## Hypothesen-Katalog (vollständig)
[Alle Hypothesen aus hypothesis-catalogue.md]

## Domänen-Findings — Explorer-Sektionen
[Pro Domäne: nur die Explorer-Sektion — Lücken, Frontier, Hypothesen, Baubarkeit]

## Vollständige Domänen-Findings
[Executive Summaries der einzelnen Findings-Dateien]

## Was nicht existiert (Frontier-Karte)
[Explizite Liste von Lücken — was wäre wertvoll aber existiert noch nicht?]

## Coordinator-Hypothesen vs. generierte Hypothesen
[Vergleich: Was hat der Coordinator vorhergesagt? Was hat die Recherche darüber hinaus gefunden?]

## Quellenqualität — Recency-Übersicht
[Anteil Quellen <6 Monate / 6-12 Monate / >12 Monate]
[Frontier-Tags Übersicht]
```

## Session-Handoff

In `context/from-human/[SLUG]/research-approach.md` ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** Generative Explorer
**Stärkste Hypothesen:** [Top 3]
**Priorisiertes Experiment:** [#1 mit kurzer Begründung]
**Nächste Session:** [Experimente ausführen? Weitere Domänen? Deep Dive in H[N]?]
**Coordinator-Überraschungen:** [Was hat die Recherche entdeckt das nicht erwartet wurde?]
```

## Deliverables-Checkliste

- [ ] `context/from-internet/sources-[DATUM].md` (Recency-Fokus, mit Datumsangaben)
- [ ] Pro Domäne: Findings-Datei MIT Explorer-Sektion
- [ ] `outputs/individual/[SLUG]/hypothesis-catalogue.md`
- [ ] `outputs/individual/[SLUG]/experiment-designs.md`
- [ ] `outputs/aggregated/mk-combined/[DATUM]-[SLUG]-explorer-report.md`
- [ ] `scratchpad/[SLUG]-coordinator-hypotheses.md`
- [ ] Research Log mit Checkpoints aktualisiert
- [ ] Session-Handoff geschrieben
- [ ] Konfidenz-Kennzeichnung bei allen Hypothesen (Hoch/Mittel/Niedrig/Spekulativ)
- [ ] Frontier-Tags in allen Quellen-Abschnitten gesetzt
