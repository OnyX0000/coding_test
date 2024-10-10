-- 코드를 입력하세요
SELECT
    p.MEMBER_NAME,
    r.REVIEW_TEXT,
    DATE_FORMAT(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM MEMBER_PROFILE p
JOIN REST_REVIEW r on r.MEMBER_ID = p.MEMBER_ID
WHERE r.MEMBER_ID = (SELECT MEMBER_ID 
                      FROM REST_REVIEW 
                      GROUP BY 1 
                      ORDER BY COUNT(MEMBER_ID) DESC 
                      LIMIT 1)
ORDER BY 3, 2