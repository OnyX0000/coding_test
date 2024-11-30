# Write your MySQL query statement below
SELECT 
    contest_id, 
    ROUND((COUNT(contest_id) / (SELECT COUNT(user_id) FROM Users) * 100), 2) as percentage 
FROM Register
GROUP BY 1
ORDER BY 2 DESC, 1 ASC