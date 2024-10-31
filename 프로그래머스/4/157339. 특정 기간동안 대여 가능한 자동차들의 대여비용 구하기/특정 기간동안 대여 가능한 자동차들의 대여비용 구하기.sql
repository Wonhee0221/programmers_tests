-- 코드를 입력하세요
/*
-3개의 테이블에서 (CAR_RENTAL_COMPANY_RENTAL_HISTORY, )
- 세단, SUV 인 자동차중 2022년 11월 1일 부터 2022년 11월 30일까지 대여가 가능하고
- 30일간의 대여 금액이 50만원 ~ 200만원 미만인 자동차
- 출력 : 자동차 ID, 자동차 종류, 대여금액(as FEE)

*/
SELECT c.car_id, c.car_type, ROUND((c.daily_FEE*30*(100-p.discount_rate)/100)) as FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS D
JOIN CAR_RENTAL_COMPANY_CAR AS C
ON D.CAR_ID = C.CAR_ID
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON
C.CAR_TYPE = P.CAR_TYPE
WHERE C.CAR_ID NOT IN (
SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE < "2022-12-01" and end_date >= "2022-11-01"
) and p.duration_type = '30일 이상'
group by c.car_id
having c.car_type in ('SUV','세단') AND (FEE >= 500000 AND FEE < 2000000)
-- 정렬 : 대여금액 DESC, 자동차종류 ASC, 자동차 ID DESC
ORDER BY FEE DESC, C.CAR_TYPE, C.CAR_ID