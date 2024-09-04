# Write your MySQL query statement below
SELECT 
    transaction_date, 
    SUM(CASE WHEN amount % 2 = 1 THEN amount ELSE 0 END) as odd_sum, 
    SUM(CASE WHEN amount % 2 = 0 THEN amount ELSE 0 END) as even_sum
FROM Transactions
GROUP BY 1
ORDER BY 1 ASC