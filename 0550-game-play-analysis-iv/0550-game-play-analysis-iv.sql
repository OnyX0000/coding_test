# Write your MySQL query statement below
SELECT 
    ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction
FROM Activity  a
INNER JOIN
    (SELECT player_id, MIN(event_date) AS min_event_date 
    FROM Activity 
    GROUP BY 1) as b
ON a.player_id = b.player_id
WHERE DATEDIFF(a.event_date, b.min_event_date) = 1