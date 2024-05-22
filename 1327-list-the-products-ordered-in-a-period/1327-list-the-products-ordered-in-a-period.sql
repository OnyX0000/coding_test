# Write your MySQL query statement below
SELECT 
    p.product_name,
    SUM(o.unit) as unit
FROM Products p
INNER JOIN Orders o on p.product_id = o.product_id and MONTH(o.order_date) = 2 and YEAR(order_date) = 2020
GROUP BY o.product_id HAVING unit >= 100