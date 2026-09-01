# aktien-retail-edge

**Status:** Pausiert (Entscheidung 2026-08-31 — Trading-Fokus liegt auf Cluster `futures-trading-edge`)
**Erstellt:** 2026-08-30
**Zuletzt aktualisiert:** 2026-08-31
**Ziel:** Einen strukturell tragfähigen Prozess + Mechanismus für kurz- bis mittelfristigen Aktienhandel eines einzelnen Retail-Traders in Deutschland mit 5.000–10.000 € Kapital erarbeiten — LLM-gestützt, mit dem Kernproblem: Firmen finden, bevor sich ihr Potential entfaltet, bei minimierter Fehlentscheidungsrate.

## Sessions

| Datum | SLUG | Typ | Status | Baut auf |
|---|---|---|---|---|
| 2026-08-30 | 2026-08-30-aktien-retail-edge-strategic | Strategic | **Complete** | 2026-03-30-agentic-trading-edge (Explorer), futures-trading-edge (Cluster, Erb-Bezug) |

**Ergebnis Session 1:** 2 Experimente (E1 Peer-Cluster-Synthetischer-Konsens, E2 Insider-Kauf-Personen-Baseline US-Pilot) nach zwei Ideengenerierungs-Durchläufen und 18 Eliminierungen. Zentrale Erkenntnis: Kleines Kapital ist ein Segment-Selektor, kein Nachteil — aber Vorteil und Transaktionskosten sitzen am selben Ort. Nächster Schritt ist ein Nullhypothesen-Test, der über die Tragfähigkeit der gesamten Ideenklasse entscheidet.

## Beziehung zu `futures-trading-edge`

Dieser Cluster ist **bewusst getrennt** vom Cluster `futures-trading-edge`, obwohl das Oberthema verwandt ist.

**Grund der Trennung (Entscheidung 2026-08-30):**
Futures sind strukturell Zero-Sum — jedem Gewinn steht ein Verlust gegenüber (dort Axiom A4).
Aktien sind es nicht: Eine Aktie ist ein Anspruch auf zukünftige Zahlungsströme, der Gesamtmarkt
kann über die Zeit wachsen. Das ist ein Unterschied auf Axiom-Ebene und verändert, was
überhaupt ein Edge *ist*. Eine Vermischung der Cluster würde Futures-Axiome stillschweigend
auf Aktien übertragen — genau der Fehler, den das Verfahren verhindern soll.

**Erb-Regel für geerbte Axiome aus `futures-trading-edge`:**
Geerbte Axiome gelten als *Kandidaten mit Prüfpflicht*, nie als gesetzte Wahrheit.
Zusätzlich gilt eine Alterungs-Unterscheidung (User-Einwand 2026-08-30):

| Typ | Beispiele | Alterung | Behandlung |
|---|---|---|---|
| **Strukturell** | Kapitaleffizienz-Constraint (A3), kognitive Grenze (A7), Informations-Zeitwert (A6) | Langsam (Jahre) | Dürfen als Kandidat durchgereicht werden, Neuprüfung auf Aktien-Anwendbarkeit |
| **Technologie-kontingent** | Was ein LLM leisten kann, welche Datenzugänge offen sind, welche Tools existieren | Schnell (Monate) | Müssen vor Verwendung neu verifiziert werden — Stand von 2026-04 ist potenziell veraltet |
| **Regulatorisch** | Steuerregeln, Haltefristen, Broker-Regeln | Kontingent, Verfallsdatum | Als Randbedingung mit Ablaufdatum führen, nie als Fundament |

## Offene Fäden

**Aus Session 1 beantwortet:**
- Zero-Sum-Frage: geklärt als Zerlegungsfrage → neues Axiom A2. Aktien sind als Instrument
  Positive-Sum, der idiosynkratische Anteil der Kursbewegung ist netto Kosten zero-sum-artig.
- Futures-Axiome: alle 9 geprüft. 3 übernommen, 4 eingeschränkt, 1 widerspricht, 1 verworfen.
- Zeithorizont 1–2 Wochen: praktisch nicht tragfähig, primär wegen Transaktionsreibung.
  Empfehlung geht Richtung mittlerer Horizont.

**Neu offen nach Session 1:**
- **Die entscheidende Frage:** Existieren im deutschen Small-Cap-Universum überhaupt
  genügend Titel mit 0–1 Analysten UND Spread <= 0,8 % UND ADV >= 150.000 €? Der
  Nullhypothesen-Test beantwortet das. Fällt er negativ aus, ist die gesamte Ideenklasse
  bei 5.000–10.000 € Kapital nicht tragfähig.
- Wie groß ist der A4-Vorteil noch, nachdem der Liquiditätsfilter die tiefsten
  Coverage-Lücken herausgeschnitten hat? Bisher nur qualitativ beantwortet.
- Ist Negativ-Selektion (Firmen ausschließen) robuster gegen LLM-Halluzination als
  Positiv-Selektion? Coordinator-Hypothese CH3, in dieser Session nicht adressiert.
- Lässt sich das Pre-Publication-Decay (70–80 % des Insider-Alphas) irgendwie umgehen,
  oder ist es eine harte Obergrenze für alle meldungsbasierten Signale?
- Produktoption: User sagte "erstmal nur Eigenkapital" — weiterhin offen, nicht bewertet.

## Cluster-Gedächtnis (Übersicht)

- **Axiom-Library:** 8 Axiome (alle Status Tentativ — Session 1) + 9 geerbte Futures-Axiome mit Prüfurteil
- **Dogma-Graveyard:** 20 Dogmen mit Gegenthesen
- **Idea-Outcomes:** 18 Ideen (2 überlebt, 16 eliminiert, 0 implementiert)

**Warnung für Folge-Sessions:** Kein Axiom ist bisher Bestätigt. Alle 8 stammen aus einer
einzigen Session und sind noch nicht unabhängig reproduziert. Der First Principles Agent
der nächsten Session muss sie explizit prüfen, nicht übernehmen.
