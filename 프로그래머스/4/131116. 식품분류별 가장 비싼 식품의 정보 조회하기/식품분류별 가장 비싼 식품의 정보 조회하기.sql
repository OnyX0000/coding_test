-- 코드를 입력하세요
SELECT
    CATEGORY,
    PRICE as MAX_PRICE,
    PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE in (
    SELECT MAX(PRICE) 
    FROM FOOD_PRODUCT 
    GROUP BY CATEGORY
) and CATEGORY in ('과자', '국', '김치', '식용유')
GROUP BY 1
ORDER BY 2 DESC