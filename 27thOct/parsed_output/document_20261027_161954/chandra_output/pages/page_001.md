## 1. Executive Summary

Northstar Sample Labs is a fictional organization used to demonstrate mixed document content. This test pack describes a small equipment-monitoring pilot, records its key metrics, and summarizes sample findings. The material intentionally includes repeated terms, identifiers, abbreviations, and values that a parser should preserve.

### Pilot overview

The pilot ran from 1 September 2026 through 30 September 2026. Three locations submitted daily sensor readings. The sample dataset contains 1,248 observations, of which 1,211 were valid and 37 were flagged for review. A flagged observation is not automatically an error; it indicates that a rule or threshold needs checking.

| Metric               | Result | Definition                        |
|----------------------|--------|-----------------------------------|
| Total observations   | 1,248  | All submitted sensor readings     |
| Valid observations   | 1,211  | Readings passing basic validation |
| Flagged observations | 37     | Readings requiring review         |
| Validation rate      | 96.9%  | Valid ÷ total × 100               |
| Locations            | 3      | North, Central, and South         |

### Key findings

- Central location recorded the highest observation count: 451.
- The average measured temperature was 21.8 °C; the maximum was 38.4 °C.
- Median network latency was 42 ms, while the 95th percentile was 118 ms.
- The largest source of flagged records was missing humidity data.

*Interpretation note: The numbers are fabricated to create realistic extraction cases. They do not represent measurements from an actual organization.*

### 2. Location Summary

| Location | Code  | Observations | Valid | Flagged |
|----------|-------|--------------|-------|---------|
| North    | LOC-N | 392          | 382   | 10      |
| Central  | LOC-C | 451          | 439   | 12      |
| South    | LOC-S | 405          | 390   | 15      |
| Total    | —     | 1,248        | 1,211 | 37      |