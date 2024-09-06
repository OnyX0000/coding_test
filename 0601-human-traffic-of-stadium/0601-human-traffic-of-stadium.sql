# Write your MySQL query statement below
WITH T1 AS (
    SELECT 
        id, 
        visit_date, 
        people,
        CASE WHEN people >= 100 THEN 1 ELSE 0 END as is_valid,
        ROW_NUMBER() OVER (ORDER BY id) - ROW_NUMBER() OVER (PARTITION BY CASE WHEN people >= 100 THEN 1 ELSE 0 END ORDER BY id) as grp
    FROM Stadium
)
SELECT id, visit_date, people
FROM T1
WHERE is_valid = 1 and grp in (SELECT grp 
                               FROM T1 
                               WHERE is_valid = 1 
                               GROUP BY grp 
                               HAVING COUNT(*) >= 3)
ORDER BY visit_date