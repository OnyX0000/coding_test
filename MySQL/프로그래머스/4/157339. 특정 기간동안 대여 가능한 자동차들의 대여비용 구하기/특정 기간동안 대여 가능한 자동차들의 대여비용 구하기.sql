-- 코드를 입력하세요
SELECT c1.CAR_ID, c1.CAR_TYPE, 
       FLOOR(c1.DAILY_FEE*30*(1-c3.DISCOUNT_RATE*0.01)) as fee
FROM CAR_RENTAL_COMPANY_CAR c1,
     CAR_RENTAL_COMPANY_RENTAL_HISTORY c2,
     CAR_RENTAL_COMPANY_DISCOUNT_PLAN c3
WHERE c1.CAR_ID = c2.CAR_ID
    and c1.CAR_TYPE = c3.CAR_TYPE
    and c1.CAR_TYPE in ('세단', 'SUV')
    and c3.DURATION_TYPE = '30일 이상'
GROUP BY c1.CAR_ID
HAVING MAX(c2.END_DATE) < '2022-11-01'
and fee >= 500000 and fee < 2000000
ORDER BY fee DESC, c1.CAR_TYPE, c1.CAR_ID DESC