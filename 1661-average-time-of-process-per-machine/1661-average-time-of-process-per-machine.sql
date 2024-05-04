# Write your MySQL query statement below
SELECT a.machine_id,
    ROUND(
      (SELECT avg(b.timestamp) FROM Activity b WHERE b.activity_type = 'end' and b.machine_id = a.machine_id) - 
      (SELECT avg(b.timestamp) FROM Activity b WHERE b.activity_type = 'start' and b.machine_id = a.machine_id), 3) as processing_time
FROM Activity a
GROUP BY a.machine_id