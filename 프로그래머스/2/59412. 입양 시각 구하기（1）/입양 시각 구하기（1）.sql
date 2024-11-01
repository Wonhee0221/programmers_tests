-- 코드를 입력하세요
/*
출력 : HOUR	COUNT
정렬 : 결과는 시간대 순
*/
SELECT date_format(datetime,"%H") as HOUR, count(*) as COUNT
FROM animal_outs
group by hour
having HOUR >= 9 and HOUR < 20
order by HOUR
