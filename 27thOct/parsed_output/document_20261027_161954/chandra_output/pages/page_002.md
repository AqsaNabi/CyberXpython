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