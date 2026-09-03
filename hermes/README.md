# Hermes Port — Strategic Innovation Pipeline

Dieser Branch (`hermes-port`) enthält die Portierung des Strategic-Innovation-Ansatzes
auf die Hermes-Agent-Architektur.

## Installierte Komponenten

- **Skill:** `~/.hermes/skills/strategic-innovation/SKILL.md` (Quelle hier gespiegelt
  unter `hermes/skills-src/strategic-innovation.md`)
- **Projektkontext:** `context/from-human/project-context.md`
- **Cronjob:** wöchentliche Hintergrund-Runde (Delivery: Telegram), siehe unten

## Lebenszyklus einer Idee (Anti-Dauerloop)

DRAFT → survived-advocatus → novelty-checked → experiment-designed →
awaiting-manual-test → TESTED-SURVIVED | TESTED-REFUTED | parked (max. 3 Code-Iterationen)

Ein Cron-Lauf = genau eine Pipeline (Phase 0–9). 0 Überlebende → kurzer Report, Ende.

## Test-Gate (QuantConnect)

Der Agent kann QC nicht selbst bedienen. Er liefert fertige Notebook-Zellen +
vorab registrierte Hypothesen nach `outputs/individual/[SLUG]/code/`.
User führt aus, legt Ergebnisse unter `outputs/individual/[SLUG]/test-results/[idea-id]/`
ab, sagt Bescheid → Auswertungs-Pass → Verdict in idea-outcomes.md.

## Modelle

Denk-Rollen: Kimi K3. Mechanik: günstiges Modell. Eskalation einzelner Schritte zu
Opus bei unauflösbaren Reasoning-Sprüngen (max. ~2/Lauf, wird geloggt → empirischer
Modellvergleich).
