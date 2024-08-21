# Write your MySQL query statement below
SELECT email as Email
FROM Person 
WHERE email is NOT NULL
GROUP BY email
HAVING COUNT(id) != 1