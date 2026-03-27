# Single-Agent Deep Dive

## Metadaten

- **Name:** Single-Agent Deep Dive
- **Am besten für:** Fokussierte Recherche in 1–2 Domänen, ohne Adversarial-Prüfung oder systematische Cross-Domain-Synthese
- **Domänen:** 1–2
- **Stakes:** Niedrig bis mittel
- **Sub-Agenten:** Nein
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

- Thema ist klar in 1–2 Wissensdomänen verortet
- Output ist keine Grundlage für Hochrisiko-Entscheidungen
- Keine systematische Gegenprüfung der Findings gewünscht
- Zeitdruck besteht (schnellster Ansatz, da kein Koordinations-Overhead)
- Erster Einstieg in ein Thema — Exploration bevor ein spezialisierter Ansatz sinnvoll ist

**Nicht verwenden wenn:**
- 3+ Domänen betroffen UND Verbindungen zwischen ihnen das eigentliche Ziel sind
- Output ist Grundlage für Entscheidungen mit hohen Konsequenzen
- Adversariale Gegenprüfung explizit gewünscht

## Selbst-Check

Vor der Ausführung prüfen:
1. Passt `context/from-human/project-context.md` zu 1–2 Domänen?
2. Sind Stakes niedrig/mittel eingeschätzt?

Falls nicht: User benachrichtigen und Approach-Auswahl neu evaluieren.

## Rollen und Modell-Zuweisungen

| Rolle | Modell | Aufgabe |
|---|---|---|
| Researcher / Coordinator | claude-sonnet-4-6 | Alle Research- und Syntheseaufgaben |

Dieser Ansatz verwendet eine einzige Instanz ohne Sub-Agenten. Alle Phasen (Recherche, Prompt-Generierung, Synthese) laufen im selben Kontext.

## Sub-Agent Invocations

Dieser Ansatz verwendet keine Sub-Agenten. Alle Arbeit wird im aktuellen Kontext ausgeführt.

## Orchestrierungs-Sequenz

### Phase 1: Kontext aufnehmen

1. Lese `context/from-human/project-context.md`
2. Lese `context/from-human/research-approach.md` (falls vorhanden — für Folge-Sessions)
3. Prüfe `context/from-history/` auf frühere Session-Transcripts
4. Lese bestehende Outputs in `outputs/individual/` (falls Folge-Session)
5. Lese `notes/research-log.md` (falls vorhanden)

### Phase 2: Prompt-Planung

1. Erstelle oder lese Recherche-Plan in `prompts/queue/research-plan.md`
2. Prüfe Prompts in `prompts/run/initial/` — falls noch keine vorhanden, generiere 3–5 initiale Prompts:
   - `01-exploratory-research.md` — Breiter Überblick über das Thema
   - `02-key-concepts.md` — Kernkonzepte und Terminologie
   - `03-current-state.md` — Aktueller Stand des Feldes
   - Weitere nach Bedarf
3. Sequenziere die Prompts: Breites zuerst, dann fokussierte Deep Dives

### Phase 3: Recherche-Ausführung

Für jeden Prompt aus der Queue:
1. Prompt ausführen — gründlich und vollständig
2. Findings sofort dokumentieren in `outputs/individual/YYYY-MM-DD-[topic].md`
3. Follow-up-Fragen identifizieren und in `prompts/run/subsequent/` speichern
4. Research Log aktualisieren: `notes/research-log.md`
5. Verbindungen zu früheren Findings notieren

**Output-Format für individual findings:**
```markdown
# [Thema] — [Datum]

## Executive Summary
[2–4 Sätze Kernaussage — wird vom Coordinator für Synthese genutzt]

## Detaillierte Findings
[Vollständige Recherche]

## Quellen / Referenzen
[Falls vorhanden]

## Offene Fragen / Follow-ups
[Generierte Follow-up-Prompts]
```

### Phase 4: Synthese

Wenn 5+ Individual-Outputs vorhanden oder eine logische Recherche-Phase abgeschlossen ist:
1. Alle Individual-Outputs lesen (Executive Summaries zuerst)
2. Aggregierten Report erstellen in `outputs/aggregated/mk-combined/YYYY-MM-DD-[topic]-report.md`
3. Report-Struktur:
   - Executive Summary (gesamte Recherche)
   - Detaillierte Findings nach Themenblock
   - Analyse und Schlussfolgerungen
   - Lücken und offene Fragen
   - Empfehlungen für nächste Recherche-Session

### Phase 5: Session-Abschluss

1. Research Log abschließen
2. Conversation-Transcript in `context/from-history/` archivieren (auf Hinweis des Users)
3. Session-Handoff in `context/from-human/research-approach.md` schreiben

## Output-Struktur

```
outputs/
├── individual/
│   └── YYYY-MM-DD-[topic].md
└── aggregated/
    └── mk-combined/
        └── YYYY-MM-DD-[project]-report.md

prompts/
├── queue/research-plan.md
└── run/
    ├── initial/01-exploratory-research.md
    └── subsequent/YYYY-MM-DD-followup-[topic].md

notes/
└── research-log.md

context/
├── from-human/research-approach.md
└── from-history/[session-transcript].md
```

## Session-Handoff

In `context/from-human/research-approach.md` nach Abschluss ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** Single-Agent Deep Dive
**Abgeschlossen:** [Was wurde recherchiert]
**Key Findings:** [3–5 Kernaussagen]
**Offene Fragen:** [Was bleibt offen]
**Nächste Schritte:** [Empfohlene nächste Prompts oder Approach-Wechsel]
```

## Deliverables-Checkliste

- [ ] Individual Findings in `outputs/individual/`
- [ ] Aggregierter Report in `outputs/aggregated/mk-combined/`
- [ ] Research Log aktualisiert in `notes/research-log.md`
- [ ] Follow-up Prompts in `prompts/run/subsequent/`
- [ ] Session-Handoff geschrieben
- [ ] Offene Fragen dokumentiert
