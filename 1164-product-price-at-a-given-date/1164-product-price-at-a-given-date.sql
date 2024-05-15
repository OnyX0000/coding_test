# Write your MySQL query statement below
SELECT DISTINCT product_id,
COALESCE((SELECT new_price
          FROM (select * from products p3 where change_date <= '2019-08-16' and p3.product_id = p2.product_id) p1
          ORDER BY change_date DESC 
          limit 1), 10) as price
FROM products p2