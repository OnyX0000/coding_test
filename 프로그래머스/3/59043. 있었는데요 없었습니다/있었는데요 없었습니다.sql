-- 코드를 입력하세요
SELECT
    i.ANIMAL_ID,
    i.NAME
FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
WHERE o.DATETIME < i.DATETIME
ORDER BY i.DATETIME