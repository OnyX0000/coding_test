# Write your MySQL query statement below
SELECT 
    customer_id,
    COUNT(v.visit_id) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t on v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL 
GROUP BY 1