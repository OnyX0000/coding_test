# Write your MySQL query statement below
SELECT 
    u.name, 
    sum(t.amount) as balance
FROM Transactions t
JOIN Users u on u.account = t.account
GROUP BY t.account
HAVING balance > 10000