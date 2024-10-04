-- 코드를 입력하세요
SELECT 
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    CASE WHEN TLNO is NULL THEN 'NONE' 
         ELSE TLNO END as TLNO
FROM PATIENT
WHERE GEND_CD = 'W' and AGE <= 12
ORDER BY 4 DESC, 1 