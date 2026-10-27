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