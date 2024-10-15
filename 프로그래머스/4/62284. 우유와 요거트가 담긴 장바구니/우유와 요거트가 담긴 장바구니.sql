-- 코드를 입력하세요
SELECT
    DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE 
    NAME = 'Milk' and CART_ID in (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = 'Yogurt'
    ) 
ORDER BY 1