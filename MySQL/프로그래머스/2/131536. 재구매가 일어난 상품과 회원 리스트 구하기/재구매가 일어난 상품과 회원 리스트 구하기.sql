-- 코드를 입력하세요
SELECT user_id, product_id
FROM (
    SELECT USER_ID, PRODUCT_ID, COUNT(*) AS p_count
    FROM ONLINE_SALE
    GROUP BY USER_ID, PRODUCT_ID
    HAVING COUNT(*) > 1
) AS re_purchase
group by user_id, product_id
order by user_id, product_id desc