# Multi-Agent Adversarial

## Metadaten

- **Name:** Multi-Agent Adversarial
- **Am besten für:** Recherche bei der Qualität und Verlässlichkeit kritisch sind — unabhängige Gegenprüfung durch einen Critic-Agenten der die Reasoning-Kette des Researchers nicht gesehen hat
- **Domänen:** 1–2 (Tiefe statt Breite)
- **Stakes:** Hoch — Output ist Entscheidungsgrundlage mit spürbaren Konsequenzen
- **Sub-Agenten:** Ja (echte Claude Code Sub-Agenten via Agent-Tool)
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

- Output wird Grundlage für Entscheidungen mit hohen finanziellen, gesundheitlichen, rechtlichen oder strategischen Konsequenzen
- Adversariale Gegenprüfung explizit gewünscht ("ich will nicht nur bestätigt werden")
- Risiko von Confirmation Bias oder einseitiger Recherche ist besonders relevant
- 1–2 Domänen — wenn 3+ Domänen mit Cross-Domain-Synthese gewünscht ist, siehe `cross-domain-synthesis.md`

**Nicht verwenden wenn:**
- Zeitdruck besteht (dieser Ansatz ist langsamer durch sequenzielle Sub-Agent-Aufrufe)
- Niedrige bis mittlere Stakes — dann ist Single-Agent effizienter
- 3+ Domänen UND cross-domain Verbindungen das Ziel

## Der Kernvorteil

Ein einzelner Claude der "sich selbst kritisiert" hat denselben blinden Fleck wie beim Erstellen des Outputs. Der Adversarial Critic in diesem Ansatz ist ein echter separater Sub-Agent mit eigenem Kontext-Fenster: Er sieht nur die finalen Findings, nicht den Reasoning-Prozess des Researchers. Dadurch kann er echte Lücken, Annahmen und Schwachstellen finden — nicht nur oberflächliche Revisionen.

## Selbst-Check

Vor der Ausführung prüfen:
1. Sind die Stakes tatsächlich hoch gemäß `context/from-human/project-context.md`?
2. Ist Adversarial-Prüfung das was der User will — oder reicht kritische Reflexion im Single-Agent-Modus?

Falls nicht: User fragen ob Downgrade auf Single-Agent sinnvoll ist.

## Rollen und Modell-Zuweisungen

| Rolle | Modell | Aufgabe |
|---|---|---|
| Research Coordinator | claude-sonnet-4-6 | Orchestrierung, Session-Management, finale Synthese |
| Domain Researcher | claude-sonnet-4-6 | Tiefe Primärrecherche zum Thema |
| Adversarial Critic | claude-sonnet-4-6 | Unabhängige Kritik der Researcher-Outputs (sieht NICHT den Reasoning-Prozess) |
| Source Gatherer | claude-haiku-4-5-20251001 | Mechanisches Sammeln von Web-Quellen nach klaren Kriterien |
| Formatter | claude-haiku-4-5-20251001 | Finales Output-Formatting und Datei-Assembly |

**Wichtig:** Adversarial Critic MUSS Sonnet sein. Haiku wäre zu flach für nicht-offensichtliche Kritik.

## Orchestrierungs-Sequenz

### Schritt 1: Vorbereitung (Coordinator)

1. Lese `context/from-human/project-context.md`
2. Lese `context/from-human/research-approach.md` (falls Folge-Session)
3. Lese bestehende Outputs in `outputs/individual/` (falls vorhanden)
4. Erstelle oder lese Recherche-Plan `prompts/queue/research-plan.md`
5. Erstelle Output-Verzeichnis `outputs/individual/` falls nicht vorhanden

### Schritt 2: Source Gathering (Haiku Sub-Agent)

Spawne Source Gatherer für mechanische Web-Recherche — siehe Sub-Agent Invocations unten.

### Schritt 3: Domain Research (Sonnet Sub-Agent)

Spawne Domain Researcher mit vollem Recherche-Auftrag — siehe Sub-Agent Invocations unten.
Warte bis Sub-Agent abgeschlossen hat und `outputs/individual/` befüllt ist.

### Schritt 4: Adversarial Critique (Sonnet Sub-Agent)

Spawne Adversarial Critic mit NUR den fertigen Outputs — kein Zugriff auf Zwischenschritte.
Warte auf Critique-Dokument in `outputs/individual/adversarial-critique.md`.

### Schritt 5: Gap Analysis (Coordinator)

1. Lese Domain Researcher Outputs + Adversarial Critique
2. Identifiziere ob kritische Lücken bestehen die eine weitere Recherche-Runde erfordern
3. Falls ja: Schritt 3–4 wiederholen mit engerer Fokussierung
4. Falls nein: Weiter zu Schritt 6

### Schritt 6: Finale Synthese (Coordinator + Formatter)

1. Coordinator erstellt Synthese-Entwurf der Researcher-Outputs UND die Critique-Response einbezieht
2. Spawne Formatter für finales Dokument-Assembly — siehe Sub-Agent Invocations unten
3. Finaler Report landet in `outputs/aggregated/mk-combined/`

---

## Sub-Agent Invocations

---

### AGENT SPAWN: Source Gatherer

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 2 — nach Vorbereitung, vor Domain Research

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Source Gatherer für ein Research-Projekt.

Lese:
- context/from-human/project-context.md

Deine Aufgabe:
Sammle relevante Quellen zum Recherche-Thema. Nutze WebSearch und WebFetch.
Für jede relevante Quelle: Titel, URL, 2-3 Satz Zusammenfassung, warum relevant.

Kriterien für Relevanz: Passt zum Thema und den Zielen in project-context.md.
Qualitätskriterien: Aktuelle Quellen bevorzugen. Primärquellen wenn möglich.

Schreibe alle Quellen nach: context/from-internet/sources-[DATUM].md

Format:
## [Quellentitel]
- URL: [url]
- Relevanz: [Warum relevant für das Thema]
- Zusammenfassung: [2-3 Sätze]

Wichtig: Bewerte NICHT die Quellen — nur sammeln und beschreiben.
Keine eigene Analyse. Das macht der Domain Researcher.
```

**Erwartete Output-Dateien:**
- `context/from-internet/sources-[DATUM].md`

**Was der Coordinator danach tut:** Gibt dem Domain Researcher den Pfad zur Sources-Datei mit.

---

### AGENT SPAWN: Domain Researcher

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 3 — nach Source Gathering

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Domain Researcher für ein Research-Projekt.

Lese:
- context/from-human/project-context.md
- context/from-internet/sources-[DATUM].md (falls vorhanden)
- prompts/queue/research-plan.md
- prompts/run/initial/ (alle Prompts)

Deine Aufgabe:
Führe eine gründliche, tiefe Recherche zum Thema durch. Für jeden Prompt aus
prompts/run/initial/ erstelle ein separates Output-Dokument.

Output-Format für jedes Dokument (speichere in outputs/individual/):
Dateiname: YYYY-MM-DD-[thema-kurz].md

# [Thema]

## Executive Summary
[2-4 Sätze Kernaussage — MUSS vorhanden sein, wird vom Coordinator gelesen]

## Detaillierte Findings
[Vollständige, gründliche Recherche. Keine Abkürzungen.]

## Annahmen und Einschränkungen
[Was hast du angenommen? Was ist der Geltungsbereich dieser Findings?]

## Quellen / Referenzen
[Referenzierte Quellen]

## Offene Fragen
[Was bleibt unklar oder wäre für eine Folge-Session relevant?]

Wichtig:
- Sei gründlich und vollständig — kürzen kann der Formatter später
- Dokumentiere explizit welche Annahmen du gemacht hast
- Das ist Primärrecherche — kein Synthese-Schritt, keine Schlussfolgerungen über mehrere Dokumente hinweg
- Schreibe am Ende eine Datei scratchpad/domain-researcher-summary.md mit einer Übersicht was du recherchiert hast
```

**Erwartete Output-Dateien:**
- `outputs/individual/YYYY-MM-DD-[thema].md` (eine pro Recherche-Einheit)
- `scratchpad/domain-researcher-summary.md`

**Was der Coordinator danach tut:** Liest alle Individual-Outputs und die Summary, dann spawnt er den Adversarial Critic.

---

### AGENT SPAWN: Adversarial Critic

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 4 — nachdem Domain Researcher fertig ist

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Adversarial Critic für ein Research-Projekt.

Lese:
- context/from-human/project-context.md
- outputs/individual/ (alle Dateien des Domain Researchers)

NICHT lesen: prompts/, scratchpad/ oder andere Zwischendateien.
Du siehst nur die fertigen Findings — nicht wie der Researcher dorthin gelangt ist.

Deine Aufgabe:
Kritisiere die Findings des Domain Researchers rigoros und konstruktiv.
Du bist kein Feind — du bist ein unabhängiger Gutachter.

Kritisiere entlang dieser Dimensionen:

1. ANNAHMEN: Welche Annahmen wurden gemacht? Sind sie gerechtfertigt?
2. LÜCKEN: Was wurde nicht untersucht? Was fehlt?
3. EINSEITIGKEIT: Gibt es alternative Perspektiven die ignoriert wurden?
4. QUELLEN: Sind die Schlussfolgerungen durch die Quellen gedeckt?
5. LOGIK: Gibt es Sprünge im Reasoning? Korrelation als Kausalität?
6. KONTEXT: Was verändert sich wenn man den Kontext anders setzt?

Format der Critique (speichere in outputs/individual/adversarial-critique.md):

# Adversarial Critique — [Datum]

## Gesamtbewertung
[1 Absatz: Wo sind die Findings stark, wo schwach?]

## Kritikpunkte

### [Kritikpunkt 1 — kurzer Titel]
**Bezieht sich auf:** [Welches Dokument / welchen Abschnitt]
**Kritik:** [Präzise Beschreibung des Problems]
**Empfehlung:** [Was sollte untersucht oder korrigiert werden?]

[Wiederhole für jeden Kritikpunkt]

## Bestätigte Stärken
[Was ist gut belegt und hält der Kritik stand?]

## Priorität der offenen Punkte
[Welche Kritikpunkte sind am wichtigsten zu adressieren?]

Wichtig:
- Sei rigoros aber fair
- Pauschalaussagen ohne Belege vermeiden
- Fokus auf substanzielle Kritik, nicht auf Stil oder Format
```

**Erwartete Output-Dateien:**
- `outputs/individual/adversarial-critique.md`

**Was der Coordinator danach tut:** Liest Critique, entscheidet ob eine weitere Researcher-Runde nötig ist, dann startet Synthese.

---

### AGENT SPAWN: Formatter

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 6 — nach finaler Synthese durch Coordinator

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Formatter für ein Research-Projekt.

Lese:
- outputs/individual/ (alle Dateien)
- scratchpad/coordinator-synthesis-draft.md (vom Coordinator erstellter Entwurf)

Deine Aufgabe:
Formatiere den Synthese-Entwurf zu einem sauberen, lesbaren Final-Report.

Regeln:
- Inhalt NICHT verändern — nur Formatierung, Struktur, Konsistenz
- Überschriften-Hierarchie konsistent halten
- Tabellen wo sinnvoll einfügen
- Redundanzen entfernen (Inhalt bleibt, Wiederholungen nicht)
- Executive Summary an den Anfang

Speichere als: outputs/aggregated/mk-combined/YYYY-MM-DD-[projektname]-final-report.md

Kein eigenes Urteil, keine eigene Analyse einfügen.
```

**Erwartete Output-Dateien:**
- `outputs/aggregated/mk-combined/YYYY-MM-DD-[projektname]-final-report.md`

---

## Fallback

Falls das Agent-Tool in dieser Session nicht verfügbar ist:
1. User benachrichtigen: "Das Agent-Tool ist nicht verfügbar. Ich führe den Multi-Agent Adversarial-Ansatz sequenziell im selben Kontext aus. Der Adversarial Critic hat dann Zugriff auf meinen gesamten Kontext — der Isolations-Vorteil echter Sub-Agenten entfällt."
2. Alle Rollen sequenziell ausführen
3. Beim Critic-Schritt explizit deklarieren: "Ich wechsle jetzt in die Adversarial Critic-Rolle und versuche die eigenen Findings kritisch zu prüfen."

## Output-Struktur

```
outputs/
├── individual/
│   ├── YYYY-MM-DD-[thema].md         # Domain Researcher Outputs
│   └── adversarial-critique.md        # Adversarial Critic Output
└── aggregated/
    └── mk-combined/
        └── YYYY-MM-DD-[projekt]-final-report.md

context/
├── from-internet/sources-[DATUM].md
└── from-human/research-approach.md

scratchpad/
├── domain-researcher-summary.md
└── coordinator-synthesis-draft.md

notes/
└── research-log.md
```

## Session-Handoff

In `context/from-human/research-approach.md` ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** Multi-Agent Adversarial
**Abgeschlossen:** [Was wurde recherchiert]
**Adversarial Findings:** [Wichtigste Kritikpunkte die adressiert wurden]
**Verbleibende offene Punkte:** [Was nicht vollständig aufgelöst wurde]
**Nächste Schritte:** [Folge-Session Empfehlungen]
```

## Deliverables-Checkliste

- [ ] Individual Research Outputs in `outputs/individual/`
- [ ] Adversarial Critique in `outputs/individual/adversarial-critique.md`
- [ ] Final Report in `outputs/aggregated/mk-combined/`
- [ ] Research Log aktualisiert
- [ ] Session-Handoff geschrieben
- [ ] Kritikpunkte im Final Report adressiert oder als offen markiert
