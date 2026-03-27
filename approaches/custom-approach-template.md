# [Approach Name] — Custom Research Approach

<!--
ANLEITUNG: Kopiere diese Datei, fülle alle Abschnitte aus, speichere sie in approaches/.
Kein Abschnitt ist optional — alle sind nötig damit Claude den Ansatz korrekt ausführt.
Zeilen in <!-- --> sind Kommentare für dich und werden von Claude ignoriert.
-->

## Metadaten

- **Name:** [Kurzer, beschreibender Name]
- **Am besten für:** [1-2 Sätze wann dieser Ansatz passt]
- **Domänen:** [Anzahl und Art der Wissensdomänen]
- **Stakes:** [niedrig / mittel / hoch]
- **Sub-Agenten:** [Ja / Nein]
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

<!-- Beschreibe konkret die Bedingungen unter denen dieser Ansatz besser ist als die Standard-Ansätze. -->

- [Bedingung 1]
- [Bedingung 2]
- [Bedingung 3]

**Nicht verwenden wenn:** [Gegenindikationen]

## Selbst-Check

<!-- Claude liest diesen Abschnitt am Anfang der Session und prüft ob der Ansatz noch passt. -->

Vor der Ausführung prüfen:
1. Passt `context/from-human/project-context.md` zu den "Wann verwenden"-Kriterien oben?
2. Sind die erwarteten Domänen/Stakes korrekt eingeschätzt?

Falls nicht: User benachrichtigen und Approach-Auswahl neu evaluieren.

## Rollen und Modell-Zuweisungen

<!-- Liste alle Rollen die in diesem Ansatz vorkommen. Mindestens eine Rolle muss vorhanden sein. -->

| Rolle | Modell | Aufgabe |
|---|---|---|
| [Rolle 1] | claude-sonnet-4-6 | [Was diese Rolle tut] |
| [Rolle 2] | claude-haiku-4-5-20251001 | [Was diese Rolle tut — nur für mechanische Tasks] |

**Modell-Regel:** Nur `claude-haiku-4-5-20251001` für mechanische, gut definierte Tasks (Dateien formatieren, Quellen sammeln nach klaren Kriterien, Dateien verschieben). Für alle Tasks die Urteilsvermögen, Analyse oder Kreativität erfordern: `claude-sonnet-4-6`.

## Orchestrierungs-Sequenz

<!-- Schritt-für-Schritt Ablauf. Nummeriere jeden Schritt. Sei präzise. -->

### Schritt 1: Vorbereitung

1. Lese `context/from-human/project-context.md`
2. Lese `context/from-human/research-approach.md` (falls vorhanden)
3. Prüfe ob Outputs aus früheren Sessions in `outputs/individual/` vorhanden sind
4. [Weitere Vorbereitungsschritte]

### Schritt 2: [Beschreibung]

[Beschreibe was in diesem Schritt passiert, wer es tut, welche Dateien entstehen]

### Schritt 3: [Beschreibung]

[...]

### Schritt N: Abschluss

1. Finalen Output schreiben nach `outputs/aggregated/mk-combined/`
2. Research Log aktualisieren in `notes/research-log.md`
3. Session-Handoff in `context/from-human/research-approach.md` aktualisieren

## Sub-Agent Invocations

<!--
Falls dieser Ansatz Sub-Agenten nutzt: Einen Block pro Rolle.
Falls kein Sub-Agent: Schreibe "Dieser Ansatz verwendet keine Sub-Agenten."
-->

---

### AGENT SPAWN: [Rollenname]

**Modell:** `claude-[haiku/sonnet]-[version]`

**Zeitpunkt:** [Nach welchem Schritt / unter welcher Bedingung wird dieser Agent gespawnt]

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist [Rollenname] für dieses Research-Projekt.

Kontext lesen:
- context/from-human/project-context.md
- [weitere Kontext-Dateien]

Deine Aufgabe:
[Präzise Beschreibung was der Agent tun soll]

Output:
[Welche Dateien schreiben, in welchem Format, mit welcher Namenskonvention]

Wichtig:
[Constraints, Qualitätsanforderungen, was der Agent NICHT tun soll]
```

**Erwartete Output-Dateien:**
- `[Pfad/zu/output1.md]`
- `[Pfad/zu/output2.md]`

**Was der Coordinator danach tut:** [Wie werden die Outputs weiterverarbeitet]

---

<!-- Wiederhole den Block für jeden weiteren Sub-Agenten -->

## Fallback

Falls das Agent-Tool in dieser Session nicht verfügbar ist:
1. User benachrichtigen: "Das Agent-Tool ist nicht verfügbar. Ich führe den [Approach Name]-Ansatz sequenziell im selben Kontext aus — ohne Isolations-Vorteile echter Sub-Agenten."
2. Alle Rollen sequenziell im aktuellen Kontext ausführen
3. Für jede Rolle den System-Prompt simulieren indem der entsprechende Abschnitt aus diesem Dokument als Instruktion verwendet wird

## Output-Struktur

<!-- Welche Dateien entstehen in welchen Verzeichnissen. -->

```
outputs/
├── individual/
│   └── [YYYY-MM-DD-topic.md]     # Pro Recherche-Einheit
└── aggregated/
    └── mk-combined/
        └── [YYYY-MM-DD-final-report.md]

notes/
└── research-log.md               # Wird kontinuierlich aktualisiert

context/from-human/
└── research-approach.md          # Session-Persistenz
```

## Session-Handoff

Nach Abschluss in `context/from-human/research-approach.md` ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** [Name dieser Datei]
**Abgeschlossen:** [Was wurde erreicht]
**Offene Fragen:** [Was bleibt für die nächste Session]
**Nächste Schritte:** [Konkrete nächste Aktionen]
```

## Deliverables-Checkliste

- [ ] Alle Findings in `outputs/individual/` gespeichert
- [ ] Aggregierter Report in `outputs/aggregated/mk-combined/`
- [ ] Research Log aktualisiert
- [ ] Session-Handoff geschrieben
- [ ] Offene Fragen dokumentiert
