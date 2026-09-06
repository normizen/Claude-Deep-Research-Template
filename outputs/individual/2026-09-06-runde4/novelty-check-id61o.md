# Novelty Check — ID61o Anker-Staffel-Kaskade

**Urteil: ÄHNLICHES EXISTIERT (Auction-Echo belegt) / NOVEL nur in der Settlement-Staffelungs-Form**

## Befunde

- **Vortex Capital Group (2026, "The 1PM Echo"):** Hat exakt die Treasury-Auktion-Echo-Mechanik getestet — 1.370 Sessions, 78 Fenster-Paare auf SPY/QQQ/IWM. Befund: Auf Coupon-Auktionstagen (13:00 ET) folgt die Equity-13:30–14:00-Bewegung der 13:00–13:30-Bewegung mit t≈+8 (SPY/QQQ/IWM +8,5/+7,9/+8,0); auf Nicht-Auktionstagen ~0. Das ist die **Auction-Echo-Variante** von ID61o — publiziert, mit öffentlich vorregistriertem Kalender (TreasuryDirect). NICHT novel als Auction-Echo.
- **CME Settlement-Dokus (EPICSANDBOX, FairValue-FAQ):** Die exakten Settlement-Zeiten sind öffentlich — Treasury-Futures Settlement 13:59:30–14:00 CT, Equity-Index-Futures 14:59:30–15:00 CT. Die **Staffelung** (Bond verankert 1h vor Equity) ist dokumentiertes Marktdesign, aber keine gefundene Arbeit nutzt die **Staffelung selbst** (ZB-Anker-Impuls diffundiert vor dem ES-Anker in ES/NQ) als kalenderfestes Intraday-Lead-Lag-Signal.

## Differenzierung

- **Belegt (nicht novel):** Auction-Echo (13:00 ET Auction → 13:30–14:00 Equity) — VCG hat das mit Trefferquoten und bps publiziert.
- **NOVEL (eng):** Die **Settlement-Staffelung** als Mechanik — ZB ist um 14:00 CT *bereits verankert* (Settlement-Preis fixiert), ES/NQ erst um 15:00 CT. Das Fenster 14:00–15:00 CT, in dem der Bond-Markt "fertig" und der Equity-Markt "noch offen" ist, als Quelle eines kalenderfesten, nicht-auktionsgebundenen Lead-Lags. Das ist eine *andere* Hypothese als das Auction-Echo (das an den Auction-Inhalt gebunden ist; die Staffelung wirkt täglich).

## Implikation für ID61o

Die Idee muss sich von der Auction-Variante (belegt) zur Staffelungs-Variante (novel) verschieben: Nicht "was passiert an Auktionstagen", sondern "was passiert im täglichen 14:00–15:00-CT-Fenster zwischen ZB- und ES-Verankerung". Hinweis des Advocatus (Vorzeichen-Regime-Instabilität) bleibt bestehen und verschärft sich: Der Staffelungs-Effekt braucht ein regime-stabiles Vorzeichen, das die Auction-Variante (inhaltlich getrieben) nicht braucht.
