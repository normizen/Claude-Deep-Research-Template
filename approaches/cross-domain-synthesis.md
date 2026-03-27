# Cross-Domain Synthesis

## Metadaten

- **Name:** Cross-Domain Synthesis
- **Am besten für:** Recherche die 3+ Wissensdomänen umspannt und bei der das eigentliche Ziel ist, Verbindungen *zwischen* den Domänen zu finden — nicht nur in jeder Domäne separat zu recherchieren
- **Domänen:** 3+ (pro Domäne ein eigener Sub-Agent)
- **Stakes:** Variabel
- **Sub-Agenten:** Ja (echte Claude Code Sub-Agenten via Agent-Tool)
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

- Thema liegt an der Schnittstelle von 3+ Feldern (z.B. Trading + Kognitionspsychologie + Spieltheorie)
- Das Ziel ist explizit: Verbindungen, Muster, Analogien ZWISCHEN den Feldern finden
- Nicht-offensichtliche Insights sind erwünscht — die aus der Überschneidung entstehen, nicht aus einer Domäne allein
- Ausreichend Zeit vorhanden (dieser Ansatz ist der aufwendigste)

**Nicht verwenden wenn:**
- Das Thema ist in Wirklichkeit 1–2 Domänen tief aber breit — dann Single-Agent
- Cross-Domain nur ein Nebenaspekt ist — dann Single-Agent mit explizitem Cross-Domain-Prompt
- Adversariale Prüfung wichtiger ist als Breite — dann Multi-Agent Adversarial

## Der Kernvorteil

Ein einzelner Agent der mehrere Domänen recherchiert bringt unbewusst seine dominierende Assoziation mit. Domain Researcher A (spezialisiert auf Trading) fragt nicht "welche kognitiven Verzerrungen liegen dem GEX-Verhalten zugrunde?" — ein Psychologie-Agent schon. Der Cross-Domain Synthesizer in diesem Ansatz bekommt unabhängig konditionierte Outputs und findet Verbindungen die kein einzelner Agent gefunden hätte.

## Selbst-Check

Vor der Ausführung prüfen:
1. Sind tatsächlich 3+ Domänen identifizierbar in `context/from-human/project-context.md`?
2. Ist das Ziel explizit cross-domain Verbindungen — nicht nur Recherche in mehreren Feldern?

Falls nicht: User fragen ob Single-Agent-Deep-Dive ausreicht.

## Rollen und Modell-Zuweisungen

| Rolle | Modell | Aufgabe |
|---|---|---|
| Research Coordinator | claude-sonnet-4-6 | Orchestrierung, Domänen-Identifikation, finale Überprüfung |
| Domain Researcher [pro Domäne] | claude-sonnet-4-6 | Tiefe Recherche in einer Domäne, unabhängig von anderen |
| Cross-Domain Synthesizer | claude-sonnet-4-6 | Findet Verbindungen, Muster, Analogien zwischen allen Domänen-Outputs |
| Web Researcher | claude-haiku-4-5-20251001 | Mechanische Web-Recherche nach konkreten Quellen |
| Formatter | claude-haiku-4-5-20251001 | Finales Dokument-Assembly |

**Hinweis zur Parallelisierung:** Konzeptionell sollten alle Domain Researcher parallel laufen. In Claude Code werden sie sequenziell gespawnt (ein Agent nach dem anderen), was denselben Effekt hat: Jeder Researcher hat sein eigenes isoliertes Kontext-Fenster ohne Kenntnis der anderen.

## Orchestrierungs-Sequenz

### Schritt 1: Vorbereitung und Domänen-Identifikation (Coordinator)

1. Lese `context/from-human/project-context.md`
2. Identifiziere die Domänen explizit — liste sie auf und bestätige mit dem User wenn unklar
3. Erstelle pro Domäne einen spezialisierten Research-Auftrag
4. Erstelle Verzeichnis `outputs/individual/[domäne]/` für jede Domäne
5. Spawne Web Researcher für allgemeine Quellen-Sammlung

### Schritt 2: Web Research (Haiku Sub-Agent)

Spawne Web Researcher für mechanisches Quellen-Sammeln — siehe Sub-Agent Invocations.

### Schritt 3: Domain Research (Sonnet Sub-Agenten — sequenziell)

Für JEDE identifizierte Domäne: Spawne einen eigenen Domain Researcher.
Warte jeweils bis der vorherige abgeschlossen hat, dann spawne den nächsten.
Jeder Researcher arbeitet isoliert — kein Zugriff auf Outputs anderer Researcher.

### Schritt 4: Cross-Domain Synthese (Sonnet Sub-Agent)

Spawne Cross-Domain Synthesizer nachdem ALLE Domain Researcher abgeschlossen haben.
Dieser Agent liest alle Domänen-Outputs und sucht explizit nach Verbindungen.

### Schritt 5: Coordinator Review

1. Lese Synthese-Output
2. Prüfe ob identifizierte Verbindungen substanziell und belegt sind
3. Falls Verbindungen unbelegt: Optionaler weiterer Domain-Research-Pass zur Verifikation
4. Koordiniere finales Dokument mit Formatter

### Schritt 6: Finales Formatting (Haiku Sub-Agent)

Spawne Formatter für sauberes Dokument-Assembly.

---

## Sub-Agent Invocations

---

### AGENT SPAWN: Web Researcher

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 2 — früh, damit Quellen für alle Domain Researcher verfügbar sind

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Web Researcher für ein Cross-Domain Research-Projekt.

Lese:
- context/from-human/project-context.md

Die Domänen dieses Projekts sind: [COORDINATOR FÜLLT EIN: kommagetrennte Liste]

Deine Aufgabe:
Sammle Quellen für jede Domäne separat. Mindestens 3 Quellen pro Domäne.
Nutze WebSearch und WebFetch.

Speichere als: context/from-internet/sources-[DATUM].md

Format:
## Domäne: [Domänenname]

### [Quellentitel]
- URL: [url]
- Relevanz: [Für welche Aspekte dieser Domäne relevant]
- Zusammenfassung: [2-3 Sätze]

Wiederhole für jede Domäne.

Markiere explizit wenn eine Quelle MEHRERE Domänen berührt — diese sind besonders wertvoll.
```

**Erwartete Output-Dateien:**
- `context/from-internet/sources-[DATUM].md`

---

### AGENT SPAWN: Domain Researcher [DOMÄNE A]

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 3 — sequenziell für jede Domäne

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Domain Researcher für die Domäne: [COORDINATOR FÜLLT EIN: Domänenname]

Dies ist ein Cross-Domain Research-Projekt. Du recherchierst AUSSCHLIESSLICH deine
zugewiesene Domäne. Kein Zugriff auf andere Domänen-Outputs — das ist gewollt.

Lese:
- context/from-human/project-context.md
- context/from-internet/sources-[DATUM].md (nur Abschnitt für deine Domäne)

Das übergeordnete Thema des Projekts: [COORDINATOR FÜLLT EIN]
Deine Domäne: [COORDINATOR FÜLLT EIN]

Deine Aufgabe:
Recherchiere deine Domäne tief und vollständig aus der Perspektive des übergeordneten Themas.
Frage: Was weiß diese Domäne über [übergeordnetes Thema]?

Speichere Findings in: outputs/individual/[domäne-kurz]/YYYY-MM-DD-[domäne]-findings.md

Format:

# [Domänenname] — Findings zum Thema [Projektthema]

## Executive Summary
[2-4 Sätze — PFLICHT, wird vom Cross-Domain Synthesizer als Einstieg genutzt]

## Kernkonzepte dieser Domäne
[Welche Konzepte und Frameworks sind in dieser Domäne relevant für das Thema?]

## Detaillierte Findings
[Vollständige Recherche in dieser Domäne]

## Domänen-spezifische Erkenntnisse
[Was ist einzigartig an der Perspektive dieser Domäne? Was würde ein Außenstehender nicht wissen?]

## Potenzielle Verbindungspunkte
[Was in dieser Domäne könnte für andere Felder relevant sein? Spekuliere ruhig — der Synthesizer prüft das.]

## Offene Fragen aus dieser Domäne
[Was bleibt unklar?]

Wichtig:
- Recherchiere NUR deine Domäne — keine Synthese mit anderen Feldern
- Der Abschnitt "Potenzielle Verbindungspunkte" ist für den Cross-Domain Synthesizer gedacht
- Sei explizit über domänen-spezifische Annahmen und Grenzen
```

**Erwartete Output-Dateien:**
- `outputs/individual/[domäne]/YYYY-MM-DD-[domäne]-findings.md`

**Hinweis:** Diesen Block für JEDE Domäne wiederholen, mit angepasstem Domänenname.

---

### AGENT SPAWN: Cross-Domain Synthesizer

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Schritt 4 — nachdem ALLE Domain Researcher abgeschlossen haben

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Cross-Domain Synthesizer für ein Research-Projekt.

Übergeordnetes Thema: [COORDINATOR FÜLLT EIN]
Recherchierte Domänen: [COORDINATOR FÜLLT EIN: kommagetrennte Liste]

Lese ALLE Domänen-Outputs:
- outputs/individual/[domäne-a]/YYYY-MM-DD-[domäne-a]-findings.md
- outputs/individual/[domäne-b]/YYYY-MM-DD-[domäne-b]-findings.md
- [weitere Domänen]

Deine Aufgabe:
Finde ECHTE Verbindungen zwischen den Domänen. Nicht nur Parallelismen — substanzielle
Verbindungen die neue Einsichten ermöglichen.

Arten von Verbindungen die wertvoll sind:
1. STRUKTURELLE ANALOGIEN: Dieselbe Struktur/Muster existiert in beiden Feldern
2. KAUSALE VERBINDUNGEN: Mechanismus aus Domäne A erklärt Phänomen in Domäne B
3. METHODISCHE ÜBERTRAGUNGEN: Tool/Methode aus Domäne A wäre in Domäne B nützlich
4. KONFLIKTPUNKTE: Wo widersprechen sich die Domänen — was bedeutet das?
5. EMERGENTE EINSICHTEN: Was wird erst sichtbar wenn man beide Domänen zusammen betrachtet?

Format (speichere in outputs/individual/cross-domain-synthesis.md):

# Cross-Domain Synthesis — [Datum]

## Executive Summary
[3-5 Sätze: Was sind die wichtigsten cross-domain Einsichten?]

## Identifizierte Verbindungen

### [Verbindung 1 — kurzer Titel]
**Typ:** [Strukturelle Analogie / Kausale Verbindung / Methodische Übertragung / Konfliktpunkt / Emergente Einsicht]
**Domänen:** [Domäne A] ↔ [Domäne B]
**Beschreibung:** [Präzise Erklärung der Verbindung]
**Belege:** [Auf welche Findings stützt sich das — mit Referenz auf Domänen-Outputs]
**Praktische Implikation:** [Was bedeutet das für das Rechercheziel?]
**Stärke der Verbindung:** [Stark belegt / Hypothetisch / Spekulativ]

[Wiederhole für jede Verbindung — mindestens 3, maximal was substanziell belegt ist]

## Überraschende Findings
[Was war am wenigsten erwartbar? Was hätte ein Single-Domain-Researcher nicht gefunden?]

## Spannungsfelder
[Wo widersprechen sich die Domänen? Wie ist das aufzulösen?]

## Synthese-Schlussfolgerungen
[Was folgt aus den Verbindungen für das übergeordnete Thema?]

## Offene Cross-Domain-Fragen
[Welche Verbindungen sind interessant aber unbelegt — für Folge-Sessions]

Wichtig:
- Unterscheide klar: "stark belegt", "hypothetisch", "spekulativ"
- Verbindungen müssen in den Domänen-Outputs verwurzelt sein — keine freien Assoziationen
- Qualität über Quantität — 3 starke Verbindungen > 10 schwache
```

**Erwartete Output-Dateien:**
- `outputs/individual/cross-domain-synthesis.md`

---

### AGENT SPAWN: Formatter

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Schritt 6 — nach Coordinator Review

**Task-Beschreibung (vollständiger Prompt an den Sub-Agenten):**

```
Du bist Formatter für ein Cross-Domain Research-Projekt.

Lese:
- outputs/individual/ (alle Findings-Dateien)
- outputs/individual/cross-domain-synthesis.md
- scratchpad/coordinator-final-notes.md (falls vorhanden)

Deine Aufgabe:
Erstelle einen strukturierten Final-Report der Domänen-Findings UND Cross-Domain-Synthesis kombiniert.

Struktur:
1. Executive Summary (aus Cross-Domain-Synthesis übernehmen)
2. Cross-Domain Verbindungen (Kernstück — aus cross-domain-synthesis.md)
3. Domänen-Findings (pro Domäne ein Abschnitt, Executive Summaries der Einzeldokumente)
4. Offene Fragen und nächste Schritte

Speichere als: outputs/aggregated/mk-combined/YYYY-MM-DD-[projektname]-final-report.md

Inhalt NICHT verändern — nur Formatierung und Struktur optimieren.
```

**Erwartete Output-Dateien:**
- `outputs/aggregated/mk-combined/YYYY-MM-DD-[projektname]-final-report.md`

---

## Fallback

Falls das Agent-Tool in dieser Session nicht verfügbar ist:
1. User benachrichtigen: "Das Agent-Tool ist nicht verfügbar. Ich führe Cross-Domain Synthesis sequenziell aus. Jede Domäne wird separat im selben Kontext recherchiert — der Isolations-Vorteil entfällt, ich werde aber explizit pro Domäne denken."
2. Für jede Domäne explizit deklarieren: "Ich recherchiere jetzt ausschließlich Domäne [X]"
3. Cross-Domain Synthesizer-Phase explizit einleiten: "Ich wechsle jetzt in die Cross-Domain-Synthesizer-Rolle"

## Output-Struktur

```
outputs/
├── individual/
│   ├── [domäne-a]/
│   │   └── YYYY-MM-DD-[domäne-a]-findings.md
│   ├── [domäne-b]/
│   │   └── YYYY-MM-DD-[domäne-b]-findings.md
│   └── cross-domain-synthesis.md
└── aggregated/
    └── mk-combined/
        └── YYYY-MM-DD-[projekt]-final-report.md

context/
├── from-internet/sources-[DATUM].md
└── from-human/research-approach.md

notes/
└── research-log.md
```

## Session-Handoff

In `context/from-human/research-approach.md` ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** Cross-Domain Synthesis
**Recherchierte Domänen:** [Liste]
**Stärkste Verbindungen gefunden:** [Top 2-3 cross-domain Insights]
**Offene Cross-Domain-Fragen:** [Was für Folge-Sessions interessant wäre]
**Nächste Schritte:** [Vertiefung bestimmter Verbindungen? Adversarial Check?]
```

## Deliverables-Checkliste

- [ ] Pro Domäne eine Findings-Datei in `outputs/individual/[domäne]/`
- [ ] Cross-Domain Synthesis in `outputs/individual/cross-domain-synthesis.md`
- [ ] Final Report in `outputs/aggregated/mk-combined/`
- [ ] Research Log aktualisiert
- [ ] Session-Handoff geschrieben
- [ ] Stärke jeder Verbindung klar markiert (belegt / hypothetisch / spekulativ)
