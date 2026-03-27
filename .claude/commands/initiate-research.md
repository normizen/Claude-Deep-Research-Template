# Initiate Deep Research Project

You are initiating a new deep research project. Follow these steps systematically:

## Step 1: Gather Research Context

First, interview the user to understand their research needs:

**Ask the following questions:**

1. **Research Topic**: What is the main topic or question you want to research?
2. **Research Objectives**: What are you hoping to learn or accomplish?
3. **Existing Knowledge**: What context or background information should I know?
4. **Scope**: Are there specific aspects to focus on or avoid?
5. **Depth**: How deep should this research go? (exploratory, comprehensive, exhaustive)
6. **Output Format**: What format do you need the final output in? (report, presentation, audio script, etc.)
7. **Timeline**: Is this research time-sensitive?
8. **Sources**: Are there specific sources or types of sources to prioritize or avoid?

## Step 1.5: Research Approach Assessment and Selection

Direkt nach Abschluss des Interviews — bevor du Dateien erstellst:

### 1. Dimensionen aus den Interview-Antworten ableiten

Analysiere die Antworten auf Fragen 1–8 und ermittle:

- **Domänen-Anzahl**: Wie viele klar abgegrenzte Wissensfelder betrifft das Thema?
- **Stakes**: Wird der Output für Entscheidungen mit hohen Konsequenzen genutzt? (finanziell, gesundheitlich, rechtlich, strategisch)
- **Cross-Domain**: Ist das Hauptziel, Verbindungen *zwischen* verschiedenen Feldern zu finden?
- **Zeitdruck**: Wurde eine dringende Timeline genannt (Tage)?

### 2. Empfehlung generieren

Wende folgende Logik an:

```
WENN Domänen >= 3 UND Cross-Domain-Synthese systematisch gewünscht:
    → cross-domain-synthesis

SONST WENN Stakes hoch ODER Adversarial-Prüfung gewünscht:
    → multi-agent-adversarial

SONST:
    → single-agent-deep-dive
```

### 3. Empfehlung ausgeben (verpflichtend in diesem Format)

```
Empfohlener Ansatz: [Name]
Begründung: [1 Satz warum dieser Ansatz passt]

Kriterien-Check:
  Domänen: [N Domänen] → [getriggert / nicht getriggert]
  Stakes: [hoch/mittel/niedrig] → [getriggert / nicht getriggert]
  Cross-Domain Synthese: [ja/nein] → [getriggert / nicht getriggert]
  Zeitdruck: [dringend/offen] → [getriggert / nicht getriggert]

Alternativen:
  - [andere Option] wäre besser wenn [Bedingung]
  - Eigener Ansatz: Ich kann einen Custom-Approach für dein spezifisches Szenario generieren

Akzeptierst du diesen Ansatz, möchtest du einen anderen wählen, oder soll ich einen Custom-Approach erstellen?
```

### 4. Auf Benutzer-Bestätigung warten

- **Bestätigung**: Weiter mit Schritt 4 (Approach-Datei lesen)
- **Andere Wahl**: User nennt Ansatz → Schritt 4 mit diesem Ansatz
- **Custom-Approach**: Lese `approaches/custom-approach-template.md`, generiere interaktiv eine neue Approach-Datei, speichere in `approaches/[beschreibender-name].md`, dann Schritt 4 mit dieser Datei

### 4. Approach-Datei vollständig lesen

Lese die gewählte Approach-Datei aus `approaches/`:
- Single-Agent: `approaches/single-agent-deep-dive.md`
- Adversarial: `approaches/multi-agent-adversarial.md`
- Cross-Domain: `approaches/cross-domain-synthesis.md`
- Custom: `approaches/[custom-datei].md`

Diese Datei definiert die Orchestrierung für alle weiteren Schritte.

### 5. Session-Kontext schreiben

Erstelle `context/from-human/research-approach.md`:

```markdown
# Research Approach Selection

## Gewählter Ansatz
[Ansatz-Name]

## Datum
[ISO-Datum]

## Kriterien die getriggert haben
- Domänen: [N] → [welche Regel]
- Stakes: [Einschätzung] → [getriggert/nicht]
- Cross-Domain: [ja/nein] → [getriggert/nicht]
- Zeitdruck: [Einschätzung] → [getriggert/nicht]

## Begründung
[Ein Absatz Erklärung]

## Modell-Zuweisungen
[Aus der Approach-Datei übernehmen]

## Approach-Datei
`approaches/[dateiname].md`

## User Override
[Nein / Ja — original war [X], User hat [Y] gewählt wegen [Grund]]
```

---

## Step 2: Create Project Context File

Based on the user's answers, create a comprehensive context file:

**File**: `context/from-human/project-context.md`

**Contents should include:**
- Research topic and main questions
- Research objectives
- Scope and boundaries
- Depth requirements
- Timeline constraints
- Source preferences
- Expected deliverables
- Any domain-specific context provided

## Step 3: Generate Initial Research Plan

Create an initial research plan file:

**File**: `prompts/queue/research-plan.md`

**Include:**
- Breakdown of main research questions
- Sub-questions to explore
- Research sequence (what to research first)
- Estimated research phases
- Key areas to investigate

## Step 4: Draft Initial Research Prompts

Based on the research plan, create 3-5 initial research prompts:

**Location**: `prompts/run/initial/`

**Files**:
- `01-exploratory-research.md` - Broad overview of the topic
- `02-key-concepts.md` - Core concepts and terminology
- `03-current-state.md` - Current understanding/state of the field
- Additional prompts as needed

Each prompt should be:
- Specific and actionable
- Focused on a particular aspect
- Designed to build on previous prompts

## Step 5: Create Research Notes Template

Initialize the research notes file:

**File**: `notes/research-log.md`

**Template:**
```markdown
# Research Log - [Topic Name]

## Project Start Date
[Date]

## Research Objectives
[From context file]

## Research Sessions

### Session 1 - [Date]
**Focus**:
**Key Findings**:
**Questions Raised**:
**Next Steps**:

[Template for additional sessions]
```

## Step 6: Set Up Scratchpad

Create a scratchpad file for working notes:

**File**: `scratchpad/working-notes.md`

## Step 7: Begin Research Execution

Ask the user: "I've set up your deep research project. Would you like me to begin executing the initial research prompts, or would you like to review and refine the research plan first?"

**If user says begin:**
1. Start with the first initial prompt
2. Document findings in `outputs/individual/`
3. Update research log in `notes/`
4. Generate follow-up prompts in `prompts/run/subsequent/`
5. Continue systematically through the research plan

**If user wants to review:**
1. Show them the research plan
2. Accept modifications
3. Update prompts accordingly
4. Then begin when ready

## Step 8: Establish Research Rhythm

Set expectations for the research workflow:

**Inform the user:**
- After each research prompt execution, findings will be documented
- Follow-up questions will be generated based on discoveries
- Regular synthesis points will aggregate findings
- They can redirect or refine research direction at any time

## Throughout Research: Maintain Documentation

- Save all outputs to appropriate directories
- Keep research log updated
- Generate follow-up prompts based on findings
- Document connections between research threads
- Archive conversation histories periodically

## Research Session Conclusion

At natural stopping points, provide:
1. Summary of findings so far
2. Outstanding questions
3. Suggested next research directions
4. Draft aggregated output if appropriate

---

**Now begin by asking the Step 1 questions to understand the user's research needs.**
