# Write your MySQL query statement below
SELECT x, y, z,
    CASE 
        WHEN (x+y) > z and (x+z) > y and (y+z) > x THEN 'Yes' 
        ELSE 'No' END as triangle
FROM Triangle 