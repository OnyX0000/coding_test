-- 코드를 작성해주세요
SELECT 
    DISTINCT a.ID, 
    a.EMAIL, 
    a.FIRST_NAME, 
    a.LAST_NAME
FROM DEVELOPERS a, SKILLCODES b
WHERE 
    (a.SKILL_CODE & b.CODE) > 0
    AND b.NAME IN ("Python", "C#")
ORDER BY 1