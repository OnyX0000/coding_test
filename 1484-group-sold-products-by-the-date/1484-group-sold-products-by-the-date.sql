# Write your MySQL query statement below
SELECT 
    sell_date, 
    COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC separator ',') as products
FROM Activities 
GROUP BY 1 
ORDER BY 1 ASC