# Projects — Cluster Memory System

## Was ist ein Cluster?

Ein **Cluster** ist ein persistenter, thematischer Wissens-Container der mehrere Research-Sessions überlebt.

| Begriff | Bedeutung | Lebensdauer |
|---|---|---|
| **Session-SLUG** | `YYYY-MM-DD-[thema]-strategic` — eine einzelne Research-Session | Eine Session |
| **Cluster-Slug** | `[thema]` — ein übergreifendes Themengebiet | Dauerhaft |

**Beispiel:** Der Cluster `trading-edge` kann die Sessions `2026-04-15-orderflow-strategic`, `2026-04-20-liquiditaet-strategic` und `2026-05-01-gex-strategic` enthalten. Jede Session baut auf dem akkumulierten Wissen des Clusters auf.

**Wichtig:** Ein Cluster ist kein Ordner für Outputs. Die eigentlichen Research-Outputs (findings, reports) bleiben in `outputs/`, `context/from-human/[SLUG]/` usw. Der Cluster speichert nur das **destillierte Wissen** — Axiome, Dogmen, Ideen-Ergebnisse — das in Folge-Sessions direkt nützlich ist.

---

## Verzeichnisstruktur

```
projects/
└── [cluster-slug]/
    ├── project.md          ← Manifest: Sessions, Beziehungen, Status
    ├── axiom-library.md    ← Bestätigte Axiome aus First-Principles-Phasen
    ├── dogma-graveyard.md  ← Verworfene Standard-Ansätze mit Begründung
    └── idea-outcomes.md    ← Ideen-Ergebnisse: was überlebt hat, was gebaut wurde
```

**Cluster-Slug-Format:** Thematisch, kein Datum, Kleinbuchstaben, Bindestriche
- Gut: `trading-edge`, `ki-bildung`, `musik-monetarisierung`, `orderflow-analyse`
- Schlecht: `2026-04-15-trading`, `Research`, `allgemein`

---

## Datei-Formate

### `project.md` — Cluster-Manifest

```markdown
# [Cluster-Name]

**Status:** Aktiv | Pausiert | Archiviert
**Erstellt:** [YYYY-MM-DD]
**Zuletzt aktualisiert:** [YYYY-MM-DD]
**Ziel:** [Was wird hier langfristig erarbeitet — 1-2 Sätze]

## Sessions

| Datum | SLUG | Typ | Status | Baut auf |
|---|---|---|---|---|
| [YYYY-MM-DD] | [session-slug] | Explorer / Strategic | Complete / Active | — oder [SLUG] |

## Offene Fäden

- [Frage oder These die noch nicht untersucht wurde]
- [Lücke die für die nächste Session relevant wäre]

## Cluster-Gedächtnis (Übersicht)

- **Axiom-Library:** [N] Axiome
- **Dogma-Graveyard:** [N] Dogmen
- **Idea-Outcomes:** [N] Ideen ([N] überlebt, [N] eliminiert, [N] implementiert)
```

---

### `axiom-library.md` — Bestätigte Axiome

Axiome sind physikalische, logische oder strukturelle Grundwahrheiten über die Domäne die nicht durch Marktdynamik, Meinung oder Konvention entfernt werden können. Sie werden einmal erarbeitet und in alle Folge-Sessions übertragen — um Reduplikation zu vermeiden.

```markdown
# Axiom-Library — [Cluster-Name]

### A[N]: [Kurztitel]
**Formulierung:** [Präzise, falsifizierbare Aussage]
**Warum Axiom:** [Begründung warum das nicht wegdiskutiert werden kann]
**Implikationen:** [Was folgt logisch daraus?]
**Entdeckt in Session:** [SLUG]
**Status:** Bestätigt | Tentativ | Widerlegt
**Widerlegungshinweis:** [Falls Widerlegt: was hat es falsifiziert?]
```

**Wichtig:** Ein Axiom mit Status "Tentativ" ist noch nicht durch mehrere unabhängige Sessions bestätigt. Der First Principles Agent soll Tentativ-Axiome in neuen Sessions explizit prüfen.

---

### `dogma-graveyard.md` — Verworfene Standard-Ansätze

Dogmen sind Überzeugungen, Heuristiken oder Praktiken in der Domäne die so weit verbreitet sind dass ihre Befolgung keinen Vorteil mehr bietet — weil alle es tun. Sie werden dokumentiert damit Folge-Sessions nicht dieselbe Analyse wiederholen.

```markdown
# Dogma-Graveyard — [Cluster-Name]

### D[N]: [Dogma-Titel]
**Das Dogma:** [Wie wird es normalerweise formuliert? Wörtlich wenn möglich.]
**Ursprung:** [Wann/wo hat diese Überzeugung begonnen? In welchem Kontext war sie sinnvoll?]
**Warum eingepreist:** [Wie verbreitet ist die Überzeugung? Warum bietet Befolgen keinen Vorteil mehr?]
**Axiomatische Prüfung:** [Hält das Dogma den Axiomen der Axiom-Library stand?]
**Gegenthese:** [Die nicht-offensichtliche, axiomatisch valide Alternative]
**Entdeckt in Session:** [SLUG]
**Kategorie:** Branchenkonsens | Fachwissen | Heuristik | Axiom-der-Praxis
```

---

### `idea-outcomes.md` — Ideen-Ergebnisse

Dokumentiert was mit Ideen aus dem Strategic-Innovation-Prozess passiert ist — sowohl was eliminiert wurde (damit es nicht erneut generiert wird) als auch was überlebt und was implementiert wurde.

```markdown
# Idea-Outcomes — [Cluster-Name]

### I[N]: [Idee-Titel]
**Kern-Idee (1 Satz):** [Was war die Idee?]
**Session:** [SLUG]
**Seed-Domänen:** [Domäne A] + [Domäne B]

**Phase 4 (Advocatus Diaboli):** Überlebt | Eliminiert | Modifiziert
**Grund:** [Warum überlebt/eliminiert/modifiziert?]

**Novelty-Check:** NOVEL | Ähnliches existiert ([Referenz]) | Bereits gebaut ([Referenz])

**Implementiert:** Ja | Nein | In Arbeit
**Ergebnis:** [Falls Ja oder In Arbeit: was ist passiert? Falls Nein: warum nicht?]

**Wert für Folge-Sessions:**
[Was soll dieser Eintrag verhindern oder ermöglichen in der nächsten Session?]
```

---

## Cluster starten

### Beim Start von `/initiate-strategic`

Der Coordinator scannt automatisch `projects/` auf existierende Cluster:

```
Falls Cluster gefunden:
  Existierende Cluster:
  [1] trading-edge — Aktiv — 3 Sessions — Zuletzt: 2026-04-20
  [2] musik-ki — Aktiv — 1 Session — Zuletzt: 2026-03-30
  [0] Neuen Cluster erstellen

User wählt eine Option.
```

**Bei existierendem Cluster:**
- Coordinator liest `axiom-library.md`, `dogma-graveyard.md`, `idea-outcomes.md`
- Zeigt Zusammenfassung: "Cluster enthält [N] Axiome, [N] Dogmen, [N] Ideen"
- First Principles Agent startet mit diesen Dateien als Kontext

**Bei neuem Cluster:**
- Coordinator leitet Cluster-Slug ab (thematisch, kein Datum)
- Erstellt `projects/[cluster-slug]/` mit leeren Vorlagen-Dateien
- Initialisiert `project.md` mit Ziel und Start-Datum

---

## Session-Ende Update-Protokoll

Am Ende jeder Strategic-Session (Phase 9) aktualisiert der Coordinator alle Cluster-Dateien.

**Reihenfolge und Zeitpunkt (progressiv — nicht nur am Ende):**

| Zeitpunkt | Was wird geschrieben | Datei |
|---|---|---|
| Nach Phase 1 | Neue Axiome (Status: Tentativ) | `axiom-library.md` |
| Nach Phase 1 | Neue Dogmen | `dogma-graveyard.md` |
| Nach Phase 2 | Domain-Usage-Tracking | `context/innovation_seeds.md` |
| Nach Phase 4 | Ideen-Ergebnisse (vorläufig: überlebt/eliminiert) | `idea-outcomes.md` |
| Nach Phase 9 | Alles finalisieren, project.md Session-Zeile, Axiome bestätigen | alle 4 Dateien |

**Warum progressiv?** Sessions können unterbrochen werden. Progressives Schreiben verhindert Datenverlust bei Session-Timeout.

---

## Beziehung zu anderen Verzeichnissen

```
projects/[cluster]/          ← Destilliertes Wissen (dauerhaft)
  axiom-library.md
  dogma-graveyard.md
  idea-outcomes.md
  project.md

context/from-human/[SLUG]/   ← Session-Kontext (pro Session)
  project-context.md
  research-approach.md

outputs/individual/[SLUG]/   ← Session-Outputs (pro Session)
  novelty-check.md
  feasibility-check.md
  experiment-designs.md

outputs/aggregated/          ← Finale Reports (pro Session)

context/from-history/        ← Archivierte abgeschlossene Sessions
```

Ein Cluster kann archiviert werden indem `project.md` auf Status "Archiviert" gesetzt wird. Die Session-Outputs in `outputs/` und `context/from-human/` werden separat in `context/from-history/` archiviert.

---

## Für neue Instanzen (neue Claude-Konversation)

Beim Start einer neuen Session in einem bestehenden Cluster:
1. `projects/[cluster-slug]/project.md` lesen → aktuellen Status und Ziel verstehen
2. `projects/[cluster-slug]/axiom-library.md` lesen → was sind die bestätigten Grundwahrheiten?
3. `projects/[cluster-slug]/dogma-graveyard.md` lesen → was wurde bereits als eingepreist identifiziert?
4. `projects/[cluster-slug]/idea-outcomes.md` lesen → welche Ideen wurden schon versucht?
5. `context/from-human/[letzter-SLUG]/research-approach.md` lesen → was war das letzte Session-Handoff?

Diese 5 Dateien geben jeder neuen Instanz den vollständigen Cluster-Kontext ohne die gesamte Research-History lesen zu müssen.
