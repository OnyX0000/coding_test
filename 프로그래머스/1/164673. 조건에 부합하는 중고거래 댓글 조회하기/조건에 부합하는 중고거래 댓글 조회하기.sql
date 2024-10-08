-- 코드를 작성해주세요
SELECT
    b.TITLE,
    b.BOARD_ID,
    r.REPLY_ID,
    r.WRITER_ID,
    r.CONTENTS,
    DATE_FORMAT(r.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_REPLY r on r.BOARD_ID = b.BOARD_ID
WHERE b.CREATED_DATE LIKE "2022-10-%"
ORDER BY r.CREATED_DATE ASC, b.TITLE ASC