# DOCUMENT PARSING TEST PACK

A synthetic multi-format PDF for testing Chandra Parser

**Purpose:** This sample combines narrative text, structured tables, bullet lists, numerical data, formulas, contact details, and layout changes. Use it to inspect extraction quality and reading order.

| Document property | Value                               |
|-------------------|-------------------------------------|
| Document ID       | DPT-2026-014                        |
| Version           | 1.2                                 |
| Created           | 27 October 2026                     |
| Content type      | Synthetic / fictional               |
| Intended use      | PDF parser and RAG pipeline testing |
| Expected pages    | 5                                   |

***Important:*** All organizations, people, contact information, and measurements in this file are fictional test data. Do not treat them as real records.

## Parsing checklist

- Extract paragraphs and section headings.
- Preserve table headers and associate each value with the correct row.
- Keep lists in the correct order.
- Retain symbols, dates, units, percentages, and currency values.
- Check whether page breaks and footer text are handled appropriately.

---

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

---

## 3. Equipment Inventory

The inventory table contains alphanumeric IDs, different units, decimal values, and status labels. During extraction, each device's identifier should remain connected to its model, location, calibration date, and status.

| Device ID | Model        | Location | Range        | Last calibrated | Status      |
|-----------|--------------|----------|--------------|-----------------|-------------|
| SNS-104   | TempSense T4 | North    | −10 to 60 °C | 2026-08-21      | Active      |
| SNS-117   | HumidPro H2  | Central  | 0–100 %RH    | 2026-08-19      | Active      |
| SNS-121   | AirMetric A7 | South    | 300–1100 hPa | 2026-08-26      | Review      |
| GW-022    | LinkHub G3   | Central  | 10/100 Mbps  | 2026-08-18      | Active      |
| SNS-133   | TempSense T4 | North    | −10 to 60 °C | 2026-08-28      | Maintenance |

### 4. Monthly Readings

The following values represent fictional monthly summaries. Decimal precision and unit symbols are intentional.

| Month          | Mean temp. (°C) | Mean humidity (%RH) | Median latency (ms) | Uptime (%) |
|----------------|-----------------|---------------------|---------------------|------------|
| June 2026      | 20.6            | 46.2                | 39                  | 99.91      |
| July 2026      | 23.9            | 43.7                | 44                  | 99.87      |
| August 2026    | 22.7            | 48.1                | 41                  | 99.94      |
| September 2026 | 21.8            | 49.5                | 42                  | 99.92      |

### 5. Review Rules

| Rule ID | Condition                       | Action                      | Severity |
|---------|---------------------------------|-----------------------------|----------|
| R-01    | Temperature < −5 °C or > 45 °C  | Verify sensor and timestamp | Medium   |
| R-02    | Humidity value is null          | Mark as incomplete          | Low      |
| R-03    | Latency > 250 ms                | Inspect gateway logs        | Medium   |
| R-04    | Duplicate device ID + timestamp | Retain one; log duplicate   | High     |

Rule notation: “<” means less than; “>” means greater than; null means no recorded value. A timestamp is stored in ISO 8601 format when available, for example 2026-09-14T10:35:00+05:30.

---

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

---

### 9. Action Register

| Action ID | Task                            | Owner role      | Due date   | Priority | State       |
|-----------|---------------------------------|-----------------|------------|----------|-------------|
| ACT-01    | Review missing humidity records | Data analyst    | 2026-11-03 | Medium   | Open        |
| ACT-02    | Inspect Central gateway logs    | IT operations   | 2026-10-30 | High     | In progress |
| ACT-03    | Confirm firmware 3.2.1          | Device engineer | 2026-11-05 | Medium   | Open        |
| ACT-04    | Recalculate validation rate     | QA reviewer     | 2026-10-29 | High     | Open        |

### 10. Contact and Reference Information

| Field             | Sample value                      |
|-------------------|-----------------------------------|
| Organization      | Northstar Sample Labs (fictional) |
| Contact person    | Jordan Example                    |
| Email             | parser-test@example.invalid       |
| Reference code    | NSL-DPT-2026-014                  |
| Document revision | 1.2 — test content                |

### 11. Extraction Test Questions

- 1 What is the document ID and version?
- 2 How many observations were flagged for review?
- 3 Which device has status “Review”?
- 4 What timestamp belongs to record REC-0003?
- 5 List the four action IDs and their due dates.
- 6 Identify the intentional inconsistency in the validation rate.

*End of document. Expected content includes headings, paragraphs, tables, bullets, numeric values, Unicode symbols (°C, –, ×, ÷), ISO-style timestamps, and a deliberate inconsistency.*