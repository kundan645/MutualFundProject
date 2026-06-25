-- 1. Top 5 funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average Returns
SELECT
    AVG(return_1yr_pct) AS avg_return_1yr
FROM fact_performance;

-- 3. Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 4. Transaction Count by Type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 5. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
-- 6. Highest 5 Year Return Funds
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 7. Average Expense Ratio
SELECT
    AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- 8. Funds by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- 9. Average Transaction Amount
SELECT
    AVG(amount_inr) AS avg_transaction_amount
FROM fact_transactions;

-- 10. Top States by Investment Amount
SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC;