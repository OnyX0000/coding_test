-- 코드를 작성해주세요
SELECT 
    SUM(g.SCORE) as SCORE,
    e.EMP_NO,
    e.EMP_NAME,
    e.POSITION,
    e.EMAIL
FROM HR_EMPLOYEES e
JOIN HR_DEPARTMENT d on d.DEPT_ID = e.DEPT_ID
JOIN HR_GRADE g on g.EMP_NO = e.EMP_NO
WHERE g.YEAR = 2022
GROUP BY 2
ORDER BY 1 DESC
LIMIT 1