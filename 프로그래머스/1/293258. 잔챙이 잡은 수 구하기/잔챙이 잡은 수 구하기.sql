-- 코드를 작성해주세요
SELECT 
    COUNT(ID) as FISH_COUNT
FROM FISH_INFO
WHERE LENGTH <= 10 or LENGTH is NULL