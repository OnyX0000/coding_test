-- 코드를 작성해주세요
SELECT
    COUNT(USER_ID) as USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021 and AGE >= 20 and AGE <= 29