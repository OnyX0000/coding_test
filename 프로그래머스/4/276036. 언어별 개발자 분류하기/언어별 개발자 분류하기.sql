-- 코드를 작성해주세요
WITH T1 as (
    SELECT 
        ID, 
        EMAIL, 
        GROUP_CONCAT(DISTINCT NAME, CATEGORY) as GROUPED
    FROM 
        SKILLCODES
    JOIN 
        DEVELOPERS
        ON DEVELOPERS.SKILL_CODE & SKILLCODES.CODE
    GROUP BY 1, 2
)
SELECT 
    CASE
        WHEN GROUPED LIKE '%Front%' and GROUPED LIKE '%Python%' THEN 'A'
        WHEN GROUPED LIKE '%C#%' THEN 'B' 
        WHEN GROUPED LIKE '%Front%' THEN 'C'
    END as GRADE,
    ID, 
    EMAIL
FROM
    T1
HAVING GRADE is not NULL
ORDER BY 1, 2