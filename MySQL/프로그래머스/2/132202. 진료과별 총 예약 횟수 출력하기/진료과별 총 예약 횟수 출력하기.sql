-- 코드를 입력하세요
SELECT MCDP_CD as '진료과 코드', count(*) as '5월예약건수'
from appointment
where apnt_ymd between '2022-05-01' and '2022-05-31'
group by MCDP_CD
order by count(*) asc, mcdp_cd asc


