### 6. Data Quality Examples

These records intentionally include a missing value, a duplicate, and a threshold violation. A parser should preserve literal values and should not silently correct them.

| Record ID | Device ID | Timestamp                 | Temperature | Humidity | Note                |
|-----------|-----------|---------------------------|-------------|----------|---------------------|
| REC-0001  | SNS-104   | 2026-09-02T09:15:00+05:30 | 22.4 °C     | 48 %RH   | Normal              |
| REC-0002  | SNS-117   | 2026-09-02T09:16:00+05:30 | 21.9 °C     | —        | Humidity missing    |
| REC-0003  | SNS-121   | 2026-09-02T09:17:00+05:30 | 47.8 °C     | 41 %RH   | Threshold review    |
| REC-0004  | SNS-104   | 2026-09-02T09:15:00+05:30 | 22.4 °C     | 48 %RH   | Potential duplicate |

### 7. Calculation Notes

*Validation rate = (valid observations / total observations) × 100*

Using the summary values:  $(1,211 \div 1,248) \times 100 \approx 97.04\%$ . The executive summary's 96.9% is intentionally included as a small inconsistency to test whether a downstream quality-control step can detect conflicting values.

*Average =  $(x_1 + x_2 + \dots + x_n) / n$*

Example: for sample readings 19.5, 20.0, 22.5, and 25.0 °C, the mean is  $(19.5 + 20.0 + 22.5 + 25.0) / 4 = 21.75$  °C.

### 8. Short Narrative and Terms

During the September review, the operations team noticed intermittent delays at the Central gateway. The delay was brief and did not correlate consistently with temperature. The team recommended checking firmware version 3.2.1, confirming the gateway clock, and repeating the latency test during the next maintenance window.

| Term | Meaning                                                             |
|------|---------------------------------------------------------------------|
| API  | Application Programming Interface                                   |
| OCR  | Optical Character Recognition                                       |
| RAG  | Retrieval-Augmented Generation                                      |
| RH   | Relative humidity                                                   |
| P95  | 95th percentile: a value at or below which 95% of observations fall |
| UTC  | Coordinated Universal Time                                          |