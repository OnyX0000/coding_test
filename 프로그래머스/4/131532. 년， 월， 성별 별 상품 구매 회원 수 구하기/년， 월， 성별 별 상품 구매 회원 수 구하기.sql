-- 코드를 입력하세요
SELECT 
    YEAR(o.SALES_DATE) as YEAR,
    MONTH(o.SALES_DATE) as MONTH,
    i.GENDER,
    COUNT(DISTINCT o.USER_ID) as USERS
FROM USER_INFO i
JOIN ONLINE_SALE o on o.USER_ID = i.USER_ID
GROUP BY 1, 2, 3
HAVING i.GENDER is NOT NULL
ORDER BY 1, 2, 3