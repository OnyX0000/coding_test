# Write your MySQL query statement below
SELECT
    id,
    CASE WHEN p_id is null THEN 'Root'
         WHEN id not in (SELECT p_id FROM Tree WHERE p_id is not null) THEN 'Leaf' 
         ELSE 'Inner' end as type
FROM Tree