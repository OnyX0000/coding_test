-- 코드를 입력하세요
SELECT
    b.AUTHOR_ID,
    a.AUTHOR_NAME,
    b.CATEGORY,
    SUM(b.PRICE * s.SALES) as TOTAL_SALES
FROM BOOK b
JOIN AUTHOR a on a.AUTHOR_ID = b.AUTHOR_ID
JOIN BOOK_SALES s on s.BOOK_ID = b.BOOK_ID
WHERE YEAR(s.SALES_DATE) = 2022 and MONTH(s.SALES_DATE) = 1
GROUP BY 1, 3
ORDER BY 1, 3 DESC