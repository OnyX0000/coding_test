# Write your MySQL query statement below
SELECT 
    u.user_id as buyer_id, 
    u.join_date, 
    COUNT(order_id) as orders_in_2019
FROM Users u
LEFT JOIN Orders o on u.user_id = o.buyer_id and YEAR(o.order_date) = 2019
GROUP BY 1
ORDER BY 1