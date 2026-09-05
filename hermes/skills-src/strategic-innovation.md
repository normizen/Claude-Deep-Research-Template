---
name: strategic-innovation
description: "Use when the user wants genuinely NEW trading/idea generation via axiomatic first-principles thinking: dogma deconstruction, cross-domain seeds, Advocatus Diaboli filtering, and test-ready code — esp. futures-trading-edge / aktien-retail-edge clusters. Runs the 9-phase pipeline with delegate_task subagents, lifecycle abort rules, and a manual QuantConnect test gate."
---

# Strategic Innovation — Hermes Edition

Port of the Strategic-Innovation approach from the Claude Deep Research Template
(`~/projects/Claude-Deep-Research-Template`, branch `hermes-port`) to Hermes Agent.

**Goal:** Not frontier documentation — genuinely new, structurally different ideas from
axioms, broken dogmas, and exotic cross-domain seeds. For the futures-trading-edge
cluster: "What remains for a retail trader with 5–10k €, 1–2 h/day, ES/NQ?"

**Canonical repo:** `~/projects/Claude-Deep-Research-Template` (branch `hermes-port`).
All state lives in that repo — this skill only orchestrates.

## MODELL-DELEGIERUNG — TECHNISCHER STAND (ehrlich, nach dem 2026-09-05-Fund)

**WICHTIG — korrigiert 2026-09-05:** Hermes' `delegate_task` (tools/delegate_tool.py)
unterstützt KEIN pro-Task-Modell-Pin. Ein `"delegation": {"model": ...}`-Feld im
Task-JSON wird still ignoriert; alle Subagenten erben `parent_agent.model`. Eine
frühere Version dieser Skill behauptete das Gegenteil ("Strict Execution Layer") —
das war FALSCH und wurde nach dem Dashboard-Befund des Users (nur Kimi sichtbar)
entfernt.

**Was technisch wirklich möglich ist:**
- **`delegation.provider/model` in `~/.hermes/config.yaml`** — global, gilt für ALLE
  Subagenten eines Laufs. Teuer (alle Rollen werden Opus, auch die mechanischen).
- **Coordinator-Session-Modell** = das einzige Modell, das man ohne Config-Änderung
  variieren kann: Denk-Rollen in der Coordinator-Session selbst ausführen (kein
  Subagent), mechanische Rollen als Subagenten.

**Bis Hermes pro-Task-Pins unterstützt (Feature-Request offen / User patcht evtl.
den Tool-Code selbst), gilt:**
- ALLE Subagenten laufen auf dem Default-Modell (kimi-k3).
- Die Tabelle unten beschreibt ROLLEN und deren Anforderungen, NICHT lauffähige
  Modell-Zuweisungen. Sie ist Vorbereitung für den Tag, an dem der Tool-Code
  pro-Task-Pins akzeptiert.
- Ein echter Dual-Modell-Advocatus ist aktuell NICHT möglich — stattdessen: zwei
  verschiedene Advocatus-PROMPTS auf demselben Modell (unterschiedliche Angriffs-
  linien als Text), dokumentiert als Prompt-Variante, NICHT als Modellvariante.

**Model Evidence Log (bereinigt):**
- 2026-09-05 Fund: Dashboard zeigte nur Kimi; Code-Inspektion bestätigte, dass
  task-level delegation.model ignoriert wird. Alle vorherigen "Opus"- und
  "Haiku"-Behauptungen waren Kimi. "A/B"-Ergebnisse gelöscht.

## Triggers

- "strategic runde", "neue ideen generieren", "/initiate-strategic", "ideen-pipeline"
- cronjob `strategic-innovation-weekly`

## Iron Rules (inherited from the template — do NOT soften)

1. **Advocatus Diaboli must NEVER read `dogma-break.md`.** He tests ideas against the
   axioms, not against the dogmas. Knowing the counter-theses makes him spare ideas that
   merely *sound* anti-dogmatic. Enforce this by simply not putting that file's content
   in his delegate_task context — with delegate_task, isolation is physical.
2. **First Principles Agent gets NO web access.** Pure cognition: what is structurally true?
3. **Every phase writes files.** No results kept only in conversation. Scratchpad paths below.
4. **Cluster memory is updated progressively**, not just at the end.
5. **The five documented data traps** (see projects/futures-trading-edge/project.md STAND
   section) must be restated in every Implementation-Designer context: no mixed price
   series, no measurement without placebo, no smoothed GEX profiles (strike level only!),
   no filters without an abstain state, no post-hoc hypotheses (predictions written
   BEFORE the test).

## Lifecycle & Abort Logic (anti-infinite-loop)

Each idea carries a state in `projects/[cluster]/idea-outcomes.md`:

```
DRAFT → survived-advocatus → novelty-checked → experiment-designed
      → awaiting-manual-test → TESTED-SURVIVED | TESTED-REFUTED
      → parked (reason required)
```

- **Max 3 code iterations per idea** without measurable progress → `parked` with reason.
  Parked ideas are listed in idea-outcomes.md and must NOT be re-discovered in future
  rounds (the Idea Generator reads this file).
- **One cron run = exactly one pipeline pass** (phases 0–9). Never chain a second round
  autonomously. Next round: next schedule or explicit user command.
- **Circuit breaker:** if 0 ideas survive the Advocatus, the run ends with a short
  report. Do NOT re-roll the idea generator in the same run.
- **Awaiting-manual-test is a terminal state for the agent.** The pipeline stops there
  and reports. It resumes only when the user drops test results (see Test Gate).

## Rollen-Anforderungen (Vorbereitung für künftige pro-Task-Pins — aktuell alle auf Default-Modell)

| Rolle | Anforderung | Gewünschtes Modell (sobald Pins möglich) | Aktuell |
|---|---|---|---|
| Coordinator (diese Session) | Orchestrierung, Synthese | moonshotai/kimi-k3 (Default) | kimi-k3 |
| First Principles Agent | härtester kognitiver Schritt | stark (kimi-k3 oder opus-5) | kimi-k3 |
| Domain Matrix Seeder | mechanische Auswahl | günstig (haiku-4.5) | kimi-k3 |
| Idea Generator | Kreativität mit Constraints | A/B-Kandidat (opus-5 vs kimi) | kimi-k3 |
| Advocatus Diaboli | nicht-offensichtliche Angriffe | stark, evtl. dual (opus-5) | kimi-k3 |
| Novelty Checker | Existenz-Check + web | günstig (haiku-4.5) | kimi-k3 |
| Deep Researcher | Machbarkeitsrecherche | stark (kimi-k3) | kimi-k3 |
| Implementation Designer | QC-Code | stark (kimi-k3) | kimi-k3 |
| Formatter | Assembly, kein Urteil | günstig (haiku-4.5) | kimi-k3 |
| Research-Assistant | Kalender/Listen-Recherche | günstig (haiku-4.5) | kimi-k3 |

**Advocatus als Prompt-Dual (machbar HEUTE):** Statt zwei Modelle (nicht möglich)
zwei UNTERSCHIEDLICHE Advocatus-Prompts auf demselben Modell — einer mit Fokus
"Größenordnung + Attribution" (Kimi-Stil), einer mit Fokus "Beobachtbarkeit +
Mechanik-Kanal" (Opus-Stil aus Runde 2). Das liefert zwei Angriffslinien, ist aber
eine PROMPT-Variante — dokumentiert als solche, niemals als Modellvergleich.

## The Pipeline

### Phase 0: Cluster Memory (Coordinator, in-session)

1. `ls projects/` in the repo; list clusters; ask user (or use cron-context default
   cluster `futures-trading-edge`).
2. Read `project.md`, `axiom-library.md`, `dogma-graveyard.md`, `idea-outcomes.md`.
3. Report: "Cluster contains N axioms, N dogmas, N ideas (states: ...)".
4. Explorer check (modes A/B/C from approaches/strategic-innovation.md): default A
   (standalone). Mode B (Explorer-Lite web scan, max 8 sources, cheap model) only if the
   user signals poor frontier knowledge.

### Phase 1: First Principles (delegate_task, strong model)

Context: project-context + axiom-library + dogma-graveyard contents. NO web.
Produces: `scratchpad/[SLUG]-axioms.md` (5–10 axioms), `scratchpad/[SLUG]-dogma-break.md`
(3–8 dogmas). Prompt template: `approaches/strategic-innovation.md` AGENT SPAWN:
First Principles Agent — copy it, fill SLUG/CLUSTER-SLUG.
Coordinator then appends new axioms (status: Tentativ) and dogmas to the cluster files.

### Phase 2: Domain Matrix Seeder (delegate_task, cheap)

Context: `context/innovation_seeds.md` + `idea-outcomes.md`. Anti-anchor protocol is
MANDATORY (exclude last-3-sessions combos, exclude tried combos, different clusters,
max contrast). Produces: `scratchpad/[SLUG]-domain-selection.md`. Coordinator updates
the usage tracking table in innovation_seeds.md.

### Phase 3: Idea Generator (single oder prompt-dual)

**HINWEIS (2026-09-05):** Ein Dual-Modell-Generator (Kimi vs. Opus) ist aktuell NICHT
möglich (kein pro-Task-Modell-Pin, siehe Abschnitt oben). Die in Runde 3 als
"A/B" gefahrenen Dateien `discovery-draft-KIMI/OPUS.md` waren beide Kimi — als
Modellvergleich ungültig, als Ideenfelder aber gültig (zwei Prompt-Varianten).

**Machbar heute:** Ein Generator, ODER zwei Generatoren mit verschiedenen PROMPTS
auf demselben Modell (z.B. einer mit Fokus "breite Diversität", einer mit Fokus
"mechanische Tiefe") — dokumentiert als Prompt-Variante, nicht Modellvariante.
Sobald der Tool-Code pro-Task-Pins akzeptiert, kann hier ein echtes Modell-A/B
stehen — die Datei-Namenskonvention (-KIMI/-OPUS) bleibt dafür reserviert.

### Phase 3 (Single-Modus): Idea Generator (delegate_task, strong)

Context: axioms.md + dogma-break.md + domain-selection.md + project-context + the
parked-ideas list. Anti-anchor constraints from the template (5 rules) apply verbatim.
Produces: `scratchpad/[SLUG]-discovery-draft.md` with 5–10 low-fidelity ideas.

### Phase 4: Advocatus Diaboli (delegate_task, strong — isolated!)

Context: discovery-draft.md + axioms.md + project-context. **NOT dogma-break.md.**
Tests: axiom violation, missing structural novelty, priced-in-ness, technical
impossibility, missing substitution resistance, AND — cluster-specific — testability
with available data (QuantConnect NDX/SPX gamma+OI, Sierra NQ exports).
Result: 2–3 surviving ideas, each with its single strongest remaining objection.
Produces: `scratchpad/[SLUG]-feasibility-pre.md`.
Circuit breaker: 0 survivors → short report, run ends.
Coordinator records preliminary outcomes in idea-outcomes.md.

### Phase 5: Novelty Checker (delegate_task, cheap + web)

Only for survivors. Existence check (implementations, papers, patents, products).
Verdict per idea: NOVEL / SIMILAR EXISTS [ref] / ALREADY BUILT [ref].
Produces: `outputs/individual/[SLUG]/novelty-check.md`.

### Phase 6: Deep Researcher (delegate_task, strong + web)

Only for NOVEL / SIMILAR ideas. Full feasibility research; MUST explicitly answer the
Advocatus' strongest objection. Produces: `outputs/individual/[SLUG]/feasibility-check.md`.

### Phase 7: Implementation Designer (delegate_task, strong)

For each survivor: full experiment design PLUS **test-ready code**:

- **QuantConnect track (default):** complete, runnable Python cell(s) for the QC cloud
  notebook environment, using QC data (option gamma, OI, price). Include in the cell
  header: hypothesis, pre-registered predictions with thresholds (Cliff's d ≥ 0.10
  convention from the cluster), placebo control, abstain-state logic, and the five
  data-traps checklist as comments. Strike-level GEX only — never smoothed profiles.

  **QC API hard rules (learned the hard way from 5 fix commits, 2026-09-03 — the user
  had to repair the cell manually; do NOT repeat these mistakes):**
  - Environment is the **Research Notebook** with a pre-existing `qb = QuantBook()`
    global — do NOT instantiate a new one, do NOT use `self.`-algorithm style, do NOT
    use argparse (notebooks have no argv). Provide a `run_qc(qb)` convenience wrapper.
  - **Python API is PEP8 snake_case**: `qb.add_future(...)`, `qb.history(...)`,
    `data_mapping_mode`, `data_normalization_mode` — NOT CamelCase C# names.
  - Futures: `qb.add_future(Futures.Indices.SP_500_E_MINI, data_mapping_mode=..., 
    data_normalization_mode=DataNormalizationMode.BACKWARDS_RATIO, ...)`.
    Continuous symbol history: `qb.history(future.symbol, start, end, Resolution.MINUTE)`.
    All contracts per day: `qb.history(FutureUniverse, future.symbol, start, end, flatten=True)`.
  - If unsure about any API call, fetch the QC docs (lean.io class reference or
    quantconnect.com/docs/v2) BEFORE writing the cell — an API guess costs the user
    a manual debug round-trip.
  - Make the cell self-contained and defensive: print data-shape checks early so a
    failure is diagnosable from stdout alone.
- **Sierra track (optional):** export/analysis script specs for the user's NQ Sierra
  Chart data (existing pipeline: import_sierra_csv.py, build_dollar_bars.py).

Produces: `outputs/individual/[SLUG]/experiment-designs.md` + code files under
`outputs/individual/[SLUG]/code/qc_[idea-id].py`.

### Phase 8: Formatter (delegate_task, cheap)

Assembles `outputs/aggregated/mk-combined/[DATE]-[SLUG]-strategic-report.md`.

### Phase 9: Cluster Memory Finalization (Coordinator)

1. Axioms: Tentativ → Bestätigt where research-supported.
2. idea-outcomes.md: set states (awaiting-manual-test etc.), Novelty verdicts.
3. project.md: add session row.
4. innovation_seeds.md: finalize tracking entries (result: gut/schwach/neutral — neutral
   until tests come back).
5. Session handoff in `context/from-human/[SLUG]/research-approach.md`.
6. `git add -A && git commit` on branch `hermes-port`.

## Manual Test Gate (QuantConnect)

The pipeline CANNOT execute tests — QC cloud notebooks need manual login/run.
Contract with the user:

1. Run ends by delivering: per surviving idea, the QC cell file(s) + hypothesis +
   pre-registered thresholds + exact instructions (which notebook, what to paste).
   Delivered to the user's Telegram as a compact checklist + the report file.
2. User runs the cells on QC, saves outputs (CSV/log/screenshot text) into the repo at
   `outputs/individual/[SLUG]/test-results/[idea-id]/`.
3. User says "testergebnisse da" (or next cron run detects new files there) → a
   **Result Evaluation** pass starts: cheap model parses results, strong model judges
   against the pre-registered thresholds → TESTED-SURVIVED / TESTED-REFUTED →
   idea-outcomes.md updated → user gets the verdict.

Never claim a test result that wasn't provided as a file. Never re-run ideation to
"fix" a refuted idea — refuted is refuted, into the graveyard logic.

## Parallelization

delegate_task children run in parallel where dependencies allow: Phase 5 (novelty) for
multiple ideas in parallel; Phase 6+7 per idea in parallel. Phases 1→2→3→4 are strictly
sequential. Keep ≤5 concurrent children.

## Reporting to the user (Telegram)

- Start: "Strategic-Runde gestartet, Cluster X, Modus A — ich melde mich mit dem Report."
- End: compact summary — N ideas generated, N survived Advocatus (titles), novelty
  verdicts, test instructions checklist, path to full report. Offer MEDIA: file for the
  aggregated report.
- Escalations used: state which step went to Opus and why.
