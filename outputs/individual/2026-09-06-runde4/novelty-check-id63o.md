# Novelty Check — ID63o Post-Anker-Sparse-Fenster

**Urteil: NOVEL (mit Einschränkung — Recherche-Lücke durch Such-Backend-Ausfall)**

## Befunde

- Die Settlement-Mechanik (15:00 CT Equity-Index-Futures, VWAP über 30s) ist dokumentiert (CME FairValue-FAQ); danach setzt das "post-close" Fenster ein, in dem Futures weiterlaufen, aber der institutionelle Cash-Bezug wegfällt.
- Vortex Capital Group (2026) dokumentiert Intraday-Momentum-Verfall und Treasury-Auktion-Echo, behandelt aber nicht das *volumen-sparse* Fenster unmittelbar nach dem 15:00-CT-Settlement als eigenes Signal-Fenster.
- Keine gefundene Arbeit formalisiert das Post-Settlement-Sparse-Fenster (15:00–15:15 CT) als konditioniertes Folgetag-Open-Signal mit vorregistrierter Earnings-Kalender-Bereinigung.

## Einschränkung

Die Novelty-Recherche war eingeschränkt (Such-Backend teilweise ausgefallen). Das Urteil NOVEL steht unter Vorbehalt einer vollständigeren Suche — die Earnings-Kontamination (15:00 CT = 16:00 ET = US-Earnings-Zeit) ist unabhängig davon dokumentiert und als Pflicht-Umbau (print-freie Kohorte) bereits im Design.

## Implikation

ID63o bleibt NOVEL, aber der Advocatus-Einwand (Earnings-Kontamination) ist der dominante Risikofaktor, nicht die Neuheit. Die Idee lebt nur mit der print-freien Kohorte als Haupttest.
