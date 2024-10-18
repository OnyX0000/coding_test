-- 코드를 입력하세요
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o on o.ANIMAL_ID = i.ANIMAL_ID
ORDER BY DATEDIFF(o.DATETIME, i.DATETIME) DESC
LIMIT 2