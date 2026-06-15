-- 1. Top 5 Funds by AUM
SELECT fund_house, MAX(aum_crore)
FROM fact_aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3. Total Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 4. Total SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Sip';

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 Funds by Sharpe Ratio
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 7. Highest Alpha Funds
SELECT scheme_name, alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;

-- 8. Highest Return Funds
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC;

-- 9. Transaction Count by Type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;