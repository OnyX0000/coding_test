-- 코드를 입력하세요
SELECT 
    FLAVOR
FROM (
    SELECT FLAVOR, TOTAL_ORDER FROM FIRST_HALF
    UNION ALL
    SELECT FLAVOR, TOTAL_ORDER FROM JULY
) AS COMBINED
GROUP BY 1
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3