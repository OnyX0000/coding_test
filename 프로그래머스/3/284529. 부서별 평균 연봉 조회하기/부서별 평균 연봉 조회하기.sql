-- 코드를 작성해주세요
SELECT
    d.DEPT_ID,
    d.DEPT_NAME_EN,
    ROUND(AVG(SAL)) as AVG_SAL
FROM HR_DEPARTMENT d
JOIN HR_EMPLOYEES e on d.DEPT_ID = e.DEPT_ID
GROUP BY 1
ORDER BY 3 DESC