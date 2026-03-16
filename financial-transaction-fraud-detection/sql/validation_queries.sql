-- Check duplicate transactions
SELECT transaction_id, COUNT(*)
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- Large transactions (possible fraud)
SELECT *
FROM transactions
WHERE amount > 5000;

-- Missing merchants
SELECT *
FROM transactions
WHERE merchant IS NULL;

-- Daily transaction volume
SELECT DATE(timestamp) AS transaction_date,
COUNT(*) AS total_transactions
FROM transactions
GROUP BY DATE(timestamp)
ORDER BY transaction_date;