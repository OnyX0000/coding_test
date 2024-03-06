-- 코드를 작성해주세요
select sum(g.score) as score, g.emp_no, e.emp_name, e.position, e.email
from hr_employees e
join hr_grade g on g.emp_no = e.emp_no
group by e.emp_no
order by sum(g.score) desc
limit 1