# Novelty Check: ID67o — Batch-minus-Marginal-Residual (BMR)

**Date:** 2026-09-06  
**Task:** Novelty existence check for BMR signal (settlement price − last continuous price as next-day reversal indicator, ES/NQ retail futures)  

---

## Search Summary

Conducted 5 web searches targeting:
1. Settlement price vs continuous price as trading signal (ES/NQ)
2. Batch/marginal pricing differentials in reversal contexts
3. CME CBOT VWAP settlement mechanics & gap relationships
4. Auction-price vs continuous-price gaps as published strategy
5. Futures settlement anomalies & next-day predictability

---

## Findings

### Known & Well-Documented
- **Settlement methodology** (CME/CBOT VWAP 30s–60s windows) is public and widely covered in institutional material.
- **Close vs settlement divergence** appears in market microstructure literature (gap trading, expiration effects, settlement procedures papers).
- **Gap trading strategies** exist across multiple retail and professional platforms (ProptradingVibes, NexusFi, Quantum Algo, ChartFanatics).

### Gap-Related Work (Closest Match)
- Academic literature on **expiration-day effects** and settlement mechanism impacts (Hsieh & Ma 2009; Wiley studies on Hong Kong, Taiwan, Australia expiration procedures).
- Derivative payoff bias research (SSRN 4562800) documents systematic drift from Thursday close to 3rd Friday open tied to settlement calculations.
- **No published retail trading strategy explicitly registers "settlement minus last continuous price" as a pre-defined signal** for next-day reversal in ES/NQ.

### Batch Auction / Microstructure Context
- Frequent batch auction research (Budish, Cramton, Shim 2015; Sour Finance perpetuals) focuses on **intraday matching design**, not daily settlement price reversals.
- Batch-minus-marginal framing is **not observed** in search results as a labeled trading signal.

---

## Verdict

**SIMILAR CONCEPT EXISTS** — with caveats.

The underlying mechanics (settlement VWAP vs chart close, price gaps, reversal tendencies) are documented in academic literature and retail gap-trading guides. However:

- **No prior-registered retail trading signal explicitly labeled "BMR"** using (settlement − last continuous price) as a conditional next-day reversal filter.
- The specific combination — treating settlement process as an "overpriced marginal check" — **appears novel** as a formalized signal.
- Closest antecedent: standard gap trading (fill probability well-known; this adds settlement-specific conditioning).

**Reference:** Gap-trading fill statistics (NexusFi, ProptradingVibes) + settlement procedure docs (CME/CBOT public) + derivative payoff bias (SSRN 4562800) show partial overlap, but no exact pre-publication of BMR as a labeled strategy.

---

## Conclusion

**PARTIALLY NOVEL / SIMILAR EXISTS (components known, formalization new).**

The settlement-minus-continuous-price differential is microstructure-level data; the reversal tendency mirrors gap-fill logic, but the explicit registration of this as a "BMR signal" for next-day retail ES/NQ trading has not been published in the sources reviewed.
