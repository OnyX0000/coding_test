-- 코드를 입력하세요
SELECT animal_type,
    CASE 
        WHEN NAME IS NULL THEN 'No name' 
        ELSE NAME 
    END AS NAME,
    sex_upon_intake
from animal_ins
order by animal_id