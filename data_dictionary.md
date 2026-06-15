# Mutual Fund Analytics Platform - Data Dictionary

## 01_fund_master.csv

* amfi_code: Unique AMFI scheme code
* fund_house: Asset Management Company
* scheme_name: Mutual fund scheme name
* category: Fund category
* sub_category: Detailed category
* expense_ratio_pct: Annual expense ratio
* risk_category: Risk classification

## 02_nav_history.csv

* amfi_code: Scheme code
* date: NAV date
* nav: Net Asset Value

## 03_aum_by_fund_house.csv

* fund_house: AMC name
* aum_crore: Assets Under Management
* date: Reporting date

## 07_scheme_performance.csv

* return_1yr_pct: 1-year return
* return_3yr_pct: 3-year return
* return_5yr_pct: 5-year return
* sharpe_ratio: Risk-adjusted return
* sortino_ratio: Downside risk-adjusted return
* alpha: Excess return over benchmark
* beta: Market sensitivity

## 08_investor_transactions.csv

* investor_id: Unique investor identifier
* transaction_date: Date of transaction
* transaction_type: SIP/Lumpsum/Redemption
* amount_inr: Transaction amount
* state: Investor state
* city: Investor city
* kyc_status: KYC verification status
