# Write your MySQL query statement below
SELECT name
FROM SalesPerson 
WHERE sales_id not in (SELECT o.sales_id 
                       FROM Orders o 
                       JOIN Company c on c.com_id = o.com_id 
                       WHERE c.name = 'RED')