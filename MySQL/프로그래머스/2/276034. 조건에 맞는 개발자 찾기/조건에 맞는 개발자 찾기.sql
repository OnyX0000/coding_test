-- 코드를 작성해주세요
select distinct id, email, first_name, last_name
from developers
where (SKILL_CODE & 256 = 256 OR SKILL_CODE & 1024 = 1024)
order by id asc