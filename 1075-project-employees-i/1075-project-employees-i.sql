# Write your MySQL query statement below
SELECT p.project_id,
    ROUND(AVG(experience_years), 2)as average_years
FROM Employee e
JOIN Project p on e.employee_id = p.employee_id
GROUP BY p.project_id