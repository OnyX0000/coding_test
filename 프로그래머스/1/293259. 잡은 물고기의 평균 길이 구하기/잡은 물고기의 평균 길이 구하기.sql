-- 코드를 작성해주세요
WITH T1 as (
    SELECT 
        ID,
        FISH_TYPE,
        CASE WHEN LENGTH is NULL or LENGTH <= 10 THEN 10 
        ELSE LENGTH END as 'LENGTH',
        TIME
    FROM FISH_INFO
)
SELECT 
    ROUND(AVG(LENGTH), 2) as AVERAGE_LENGTH
FROM T1