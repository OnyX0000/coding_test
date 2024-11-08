# Write your MySQL query statement below
SELECT 
    ROUND(SUM(tiv_2016), 2) as tiv_2016
FROM Insurance
WHERE tiv_2015 in (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY 1
    HAVING COUNT(*) > 1
)
and (lat, lon) in (
    SELECT lat, lon
    FROM Insurance
    GROUP BY 1, 2
    HAVING COUNT(*) = 1
)