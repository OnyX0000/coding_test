# Write your MySQL query statement below
SELECT 
    s.student_id,
    s.student_name,
    j.subject_name,
    COUNT(e.subject_name) as attended_exams
FROM Students s
JOIN Subjects j LEFT JOIN Examinations e on s.student_id = e.student_id and j.subject_name = e.subject_name
GROUP BY 1, 3
ORDER BY 1 ASC, 3 ASC