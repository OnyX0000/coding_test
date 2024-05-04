# Write your MySQL query statement below
SELECT a.Id
FROM Weather a
WHERE EXISTS (
    SELECT id
    FROM Weather b
    WHERE a.temperature > b.temperature
    and a.recordDate=b.recordDate + INTERVAL 1 DAY
)