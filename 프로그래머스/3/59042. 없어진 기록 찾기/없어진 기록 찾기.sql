-- 코드를 입력하세요
## 입양을 갔는데, 보호소의 없는 기록/ 동물id(정렬), 이름
SELECT a.ANIMAL_ID, a.NAME
from ANIMAL_OUTS a left outer join ANIMAL_INS i on a.ANIMAL_ID = i.ANIMAL_ID
where INTAKE_CONDITION is null
order by a.ANIMAL_ID