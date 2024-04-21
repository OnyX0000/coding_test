-- 코드를 입력하세요
SELECT ai.ANIMAL_ID,
       ai.ANIMAL_TYPE,
       ai.NAME
FROM ANIMAL_INS ai INNER JOIN ANIMAL_OUTS ao on ai.ANIMAL_ID=ao.ANIMAL_ID
WHERE ai.SEX_UPON_INTAKE LIKE '%Intact%' and ao.SEX_UPON_OUTCOME NOT LIKE '%Intact%'