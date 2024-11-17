# Write your MySQL query statement below
SELECT 
    product_id, 
    product_name 
FROM Product 
WHERE product_id in (
    SELECT product_id 
    FROM Sales 
    WHERE sale_date BETWEEN '2019-01-01' and '2019-03-31'
) 
and product_id NOT IN (
    SELECT product_id 
    FROM Sales 
    WHERE sale_date NOT BETWEEN '2019-01-01' and '2019-03-31'
)