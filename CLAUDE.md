# CLAUDE.md - Deep Research Repository Instructions

## Purpose

This repository implements the Claude Deep Research Model - a structured approach to conducting comprehensive research using Claude Code.

## Research Workflow

When operating in this repository, you (Claude) should follow this workflow:

### 1. Context Gathering Phase
- Review materials in `context/` directories
- Read user-provided background from `context/from-human/`
- Process any internet research in `context/from-internet/`
- Check historical context in `context/from-history/`

### 2. Prompt Planning Phase
- Draft research prompts in `prompts/drafting/`
- Organize them by research depth and sequence
- Move finalized prompts to `prompts/queue/`

### 3. Research Execution Phase
- Execute initial exploratory prompts from `prompts/run/initial/`
- Generate follow-up questions based on findings
- Store follow-ups in `prompts/run/subsequent/`
- Document findings in real-time

### 4. Output Generation Phase
- Save individual research outputs to `outputs/individual/`
- Aggregate related findings in `outputs/aggregated/`
- Generate synthesized reports
- Create reformatted versions (TTS, SSML) in `outputs/reformatted/`

### 5. Documentation Phase
- Keep research notes in `notes/`
- Document methodology decisions
- Track research threads and connections

## Directory Structure

```
├── context/              # Research context and source materials
│   ├── from-internet/   # Web research, papers, articles
│   ├── from-human/      # User-provided context and requirements
│   ├── from-history/    # Previous conversation histories
│   └── innovation_seeds.md  # 30 exotische Domänen für Strategic Innovation Seeding
├── projects/             # Cluster Memory — persistente Themen-Container
│   └── [cluster-slug]/  # Pro Cluster: project.md, axiom-library.md, dogma-graveyard.md, idea-outcomes.md
├── prompts/             # Research prompts by stage
│   ├── drafting/        # Draft prompts
│   ├── queue/           # Prompts ready to execute
│   └── run/             # Executed prompts
│       ├── initial/     # Starting prompts
│       └── subsequent/  # Follow-up prompts
├── outputs/             # Research outputs
│   ├── individual/      # Single-topic outputs
│   ├── aggregated/      # Synthesized outputs
│   │   ├── pdf/        # PDF reports
│   │   ├── mk-combined/# Combined markdown
│   │   └── diagram-enrichments/
│   └── reformatted/     # Alternative formats
│       ├── tts-safe-txt/
│       └── ssml/
├── pipeline/            # Workflow automation
│   └── audio-dropoff/  # Audio processing queue
├── approaches/          # Reusable research approach templates
│   ├── README.md
│   ├── single-agent-deep-dive.md
│   ├── multi-agent-adversarial.md
│   ├── cross-domain-synthesis.md
│   ├── generative-explorer.md
│   ├── strategic-innovation.md
│   └── custom-approach-template.md
├── notes/              # Research notes and documentation
└── scratchpad/         # Working area for experiments
```

## Research Approach Assessment

Nach dem `/initiate-research`-Interview analysierst du automatisch die Anfrage und empfiehlst den passenden Recherche-Ansatz. Die vollständigen Ansatz-Spezifikationen liegen in `approaches/`.

### Verfügbare Ansätze

| Ansatz | Datei | Am besten für |
|---|---|---|
| Single-Agent Deep Dive | `approaches/single-agent-deep-dive.md` | 1–2 Domänen, kein Adversarial nötig — **Default** |
| Multi-Agent Adversarial | `approaches/multi-agent-adversarial.md` | High-Stakes, Gegenprüfung gewünscht |
| Cross-Domain Synthesis | `approaches/cross-domain-synthesis.md` | 3+ Domänen, Verbindungen zwischen Feldern gesucht |
| Generative Explorer | `approaches/generative-explorer.md` | Neue Möglichkeiten entdecken, Hypothesen entwickeln, Experimente designen — schnell bewegende Felder, Explorer-Modus |
| Strategic Innovation | `approaches/strategic-innovation.md` | Axiomatisches Erstprinzipiendenken + Dogmen-Dekonstruktion — genuine neue Ideen aus Grundsätzen, nicht Frontier-Dokumentation |

### Assessment-Kriterien

Bewerte nach dem Interview 5 Dimensionen und wende folgende Logik an:

```
WENN Ziel ist axiomatisches Grundsatzdenken / Dogmen brechen / genuine neue Mechaniken:
    → strategic-innovation

SONST WENN Ziel ist neue Möglichkeiten entdecken / Hypothesen entwickeln / Explorer-Modus:
    → generative-explorer

SONST WENN Domänen >= 3 UND Cross-Domain-Synthese systematisch gewünscht:
    → cross-domain-synthesis

SONST WENN Stakes hoch ODER Adversarial-Prüfung gewünscht:
    → multi-agent-adversarial

SONST WENN Zeitdruck dringend (Tage):
    → single-agent-deep-dive

SONST:
    → single-agent-deep-dive  (sicherer Default)
```

**Dimensionen:**

| Dimension | Signal im Interview | Schwellwert |
|---|---|---|
| Innovation-Modus | Ziele, Formulierung | "axiom", "grundsatz", "was ist wirklich wahr", "dogma", "genuinely new", "erste prinzipien", "eingepreist" |
| Explorer-Modus | Ziele, Formulierung | "neue Möglichkeiten", "was können wir bauen", "kreativ", "über den Tellerrand" |
| Domänen-Anzahl | Thema, Scope | ≥ 3 klar abgegrenzte Wissensfelder |
| Stakes | Ziele, Verwendungszweck | Output ist Entscheidungsgrundlage mit hohen Konsequenzen |
| Cross-Domain | Ziele, Output-Format | Verbindungen *zwischen* Feldern sind das Hauptziel |
| Zeitdruck | Timeline | Tage statt Wochen oder offen |

### Empfehlungs-Format (verpflichtend)

Die Empfehlung muss immer folgendes Format haben:

```
Empfohlener Ansatz: [Name]
Begründung: [1 Satz]

Kriterien-Check:
  Domänen: [N] → [getriggert / nicht getriggert]
  Stakes: [hoch/mittel/niedrig] → [getriggert / nicht getriggert]
  Cross-Domain: [ja/nein] → [getriggert / nicht getriggert]
  Zeitdruck: [dringend/mittel/offen] → [getriggert / nicht getriggert]

Alternative: [anderer Ansatz] wäre geeignet wenn [Bedingung].
```

### Regeln

- **Immer erklären** welche Kriterien getriggert haben — kein stilles Anwenden
- **User kann immer übersteuern** — Empfehlung ist Vorschlag, nicht Entscheidung
- **Custom Approach** — falls User einen eigenen Ansatz möchte, lies `approaches/custom-approach-template.md` und generiere eine neue Datei in `approaches/`
- **Nach Auswahl** — schreibe `context/from-human/research-approach.md` mit Ansatz, Kriterien, Modell-Zuweisungen, bevor du mit Schritt 2 weitergehst
- **Folge-Sessions** — lies `context/from-human/research-approach.md` zu Beginn; Ansatz bleibt konsistent außer User ändert ihn explizit

### Modell-Zuweisungen (für alle Multi-Agent-Ansätze)

| Rolle | Modell |
|---|---|
| Research Coordinator, Domain Researcher, Adversarial Critic, Cross-Domain Synthesizer | `claude-sonnet-4-6` |
| Source Gatherer, Web Researcher, Formatter, File Manager | `claude-haiku-4-5-20251001` |

Falls ein Modell nicht verfügbar ist: Fehler melden, nicht still degradieren.

---

## Behavioral Guidelines

### Deep Research Mode
When the user invokes `/initiate-research` or is clearly conducting deep research:

1. **Be Systematic**: Follow the research workflow methodically
2. **Be Thorough**: Don't skip steps, explore thoroughly
3. **Document Everything**: Save insights, questions, and findings
4. **Ask Clarifying Questions**: When research direction is unclear
5. **Generate Follow-ups**: Proactively identify knowledge gaps
6. **Synthesize Regularly**: Combine findings into coherent outputs

### Strategic Innovation Mode
When the user invokes `/initiate-strategic`:

1. **Adaptive Interview First**: Never use a fixed question list — follow up vague answers immediately before proceeding
2. **Distinguish Axiom from Dogma**: An axiom cannot be argued away; a dogma is a convention that has been priced in — make this distinction explicit when the user conflates them
3. **Cluster Memory is Critical**: Always check `projects/` before starting; always update cluster files at session end (progressively, not just at the very end)
4. **Explorer-Check Before Interview**: Offer Modus A/B/C before diving into axiomatic analysis — token budget matters
5. **Anti-Anchor Discipline**: The Domain Matrix Seeder must document why it chose each domain; selection without reasoning is invalid
6. **Advocatus is Destructive by Design**: Phase 4 must eliminate, not soften — an idea that survives must have passed all 5 criteria, not "mostly passed"

### File Management
- Use descriptive filenames with dates: `2025-11-02-topic-name.md`
- Keep raw research separate from synthesized outputs
- Archive completed research in appropriate directories
- Maintain clear connections between prompts and outputs

### Output Quality
- Generate comprehensive, well-structured outputs
- Include citations and source references
- Create both detailed and summary versions
- Format outputs for multiple use cases (reading, TTS, PDF)

### Research Depth
- Start broad, then narrow based on findings
- Follow promising threads deeply
- Document dead ends to avoid repetition
- Build on previous research iterations

## Slash Commands

Available slash commands for this repository:

- `/initiate-research` - Start a new deep research project
- `/initiate-explorer` - Start a new Generative Explorer project
- `/initiate-strategic` - Start a new Strategic Innovation project
- `/generate-audio` - Generate audio from a research report
- Add custom commands in `.claude/commands/`

## Working with Agents

Spezialisierte Agenten-Rollen in `.claude/agents/` (Rollenbeschreibungen):
- Research Coordinator
- Output Synthesizer / Research Synthesizer
- Prompt Generator

**Echte Sub-Agenten** werden in Multi-Agent-Ansätzen via Claude Code Agent-Tool gespawnt. Die genauen Invocation-Blöcke (Modell, Zeitpunkt, vollständiger Prompt) stehen in den jeweiligen Approach-Dateien unter `approaches/`. Sub-Agenten sind keine Rollensimulation — jeder hat ein eigenes Kontext-Fenster und arbeitet isoliert.

Verzeichnis `approaches/` enthält reusable Ansatz-Templates:
- `approaches/single-agent-deep-dive.md`
- `approaches/multi-agent-adversarial.md`
- `approaches/cross-domain-synthesis.md`
- `approaches/generative-explorer.md`
- `approaches/strategic-innovation.md`
- `approaches/custom-approach-template.md`

**Cluster-Memory-System** (`projects/`): Strategic Innovation nutzt persistente Cluster-Container die Axiome, Dogmen und Ideen-Ergebnisse über Sessions hinweg speichern. Dokumentation in `projects/README.md`.

## Best Practices

1. **Always start with context** - Review existing materials before researching
2. **Document the journey** - Notes are as valuable as outputs
3. **Version your prompts** - Track how research questions evolve
4. **Synthesize regularly** - Don't wait until the end to aggregate
5. **Use the scratchpad** - Experiment freely without cluttering main outputs

## Integration with Pipeline

The `pipeline/` directory supports automated workflows:
- Audio research inputs can be dropped in `pipeline/audio-dropoff/in-queue/`
- Processed transcripts move to `pipeline/audio-dropoff/processed/`
- Extend with your own automation scripts

## Deliverables

At the end of a research session, ensure:
- [ ] Individual findings documented in `outputs/individual/`
- [ ] Aggregated report in `outputs/aggregated/mk-combined/`
- [ ] PDF version generated in `outputs/aggregated/pdf/`
- [ ] Research notes updated in `notes/`
- [ ] Conversation history archived in `context/from-history/`
- [ ] Outstanding questions documented for next session
