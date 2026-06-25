# Mutual Fund Analytics Project - Data Dictionary

## Source Datasets

### 01_fund_master.csv

Source: Mutual Fund Master Data

| Column            | Data Type | Description                   |
| ----------------- | --------- | ----------------------------- |
| amfi_code         | INTEGER   | Unique AMFI scheme identifier |
| fund_house        | TEXT      | Asset Management Company name |
| scheme_name       | TEXT      | Mutual fund scheme name       |
| category          | TEXT      | Fund category                 |
| sub_category      | TEXT      | Fund sub-category             |
| plan              | TEXT      | Direct/Regular plan           |
| launch_date       | DATE      | Fund launch date              |
| benchmark         | TEXT      | Benchmark index               |
| expense_ratio_pct | REAL      | Expense ratio percentage      |
| fund_manager      | TEXT      | Fund manager name             |
| risk_category     | TEXT      | Risk classification           |

---

### 02_nav_history.csv

Source: NAV Historical Data

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | INTEGER   | Scheme identifier |
| date      | DATE      | NAV date          |
| nav       | REAL      | Net Asset Value   |

---

### 07_scheme_performance.csv

Source: Performance Dataset

| Column            | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| return_1yr_pct    | REAL      | One year return         |
| return_3yr_pct    | REAL      | Three year return       |
| return_5yr_pct    | REAL      | Five year return        |
| benchmark_3yr_pct | REAL      | Benchmark return        |
| alpha             | REAL      | Alpha ratio             |
| beta              | REAL      | Beta ratio              |
| sharpe_ratio      | REAL      | Sharpe ratio            |
| sortino_ratio     | REAL      | Sortino ratio           |
| aum_crore         | REAL      | Assets under management |
| expense_ratio_pct | REAL      | Expense ratio           |
| risk_grade        | TEXT      | Risk category           |

---

### 08_investor_transactions.csv

Source: Investor Transaction Data

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Investor identifier        |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme identifier          |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption |
| amount_inr         | REAL      | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age bracket       |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income              |
| payment_mode       | TEXT      | Payment method             |
| kyc_status         | TEXT      | Verified / Pending         |

---

## Database

Database Name:
bluestock_mf.db

Tables:

* dim_fund
* dim_date
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

---

## Data Quality Checks Performed

1. Date parsing completed.
2. Duplicate records removed.
3. NAV values validated (> 0).
4. Transaction amounts validated (> 0).
5. KYC status verified.
6. Return columns converted to numeric.
7. Expense ratio validated (0.1% - 2.5%).
8. AMFI code validation completed.
