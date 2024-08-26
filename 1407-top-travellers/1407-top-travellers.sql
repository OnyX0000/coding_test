# Write your MySQL query statement below
SELECT 
    u.name, 
    CASE WHEN u.id not in (SELECT user_id FROM Rides) THEN 0
         ELSE SUM(r.distance) END as travelled_distance
FROM Rides r
RIGHT JOIN Users u on u.id = r.user_id
GROUP BY r.user_id
oRDER BY 2 DESC, 1 ASC