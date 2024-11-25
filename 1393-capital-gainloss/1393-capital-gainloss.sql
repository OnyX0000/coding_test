# Write your MySQL query statement below
WITH T1 AS (
    SELECT 
        stock_name,
        SUM(CASE WHEN operation = 'Buy' THEN price ELSE 0 END) as total_buy,
        SUM(CASE WHEN operation = 'Sell' THEN price ELSE 0 END) as total_sell
    FROM Stocks
    GROUP BY 1
)
SELECT 
    stock_name, 
    (total_sell - total_buy) as capital_gain_loss
FROM T1