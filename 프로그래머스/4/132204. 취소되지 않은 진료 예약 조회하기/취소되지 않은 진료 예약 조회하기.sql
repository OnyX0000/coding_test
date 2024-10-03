-- 코드를 입력하세요
SELECT
    a.APNT_NO,
    p.PT_NAME,
    p.PT_NO,
    a.MCDP_CD,
    d.DR_NAME,
    a.APNT_YMD
FROM APPOINTMENT a
JOIN DOCTOR d on d.DR_ID = a.MDDR_ID
JOIN PATIENT p on p.PT_NO = a.PT_NO
WHERE DATE_FORMAT(a.APNT_YMD, '%Y-%m-%d') = '2022-04-13' and a.APNT_CNCL_YN = 'N'
ORDER BY 6 ASC