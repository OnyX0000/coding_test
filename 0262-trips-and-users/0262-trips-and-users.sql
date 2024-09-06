# Write your MySQL query statement below
WITH T1 as
(
    SELECT * 
    FROM Trips
    WHERE client_id not in (SELECT users_id FROM Users WHERE role = 'client' and banned = 'Yes')
),
T2 as (
    SELECT *
    FROM T1
    WHERE driver_id not in (SELECT users_id FROM Users WHERE role = 'driver' and banned = 'Yes')
)
SELECT 
    request_at as Day,
    ROUND(SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) / COUNT(id), 2) AS 'Cancellation Rate'
FROM T2 
WHERE request_at between '2013-10-01' and '2013-10-03'
GROUP BY 1