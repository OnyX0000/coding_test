SELECT LEFT(price, 1)*10000 "price_group", count(*) "count"
FROM product
GROUP BY price_group  
ORDER BY price_group