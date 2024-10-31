-- 코드를 작성해주세요
/*
테이블 : SKILLCODES, DEVELOPERS
문제 : DEVELOPERS 테이블에서 FRONT END 스킬을 가진 개발자 정보조회
출력 : ID, 이메일, 이름, 성
정렬 : ID ASC
*/
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS 
WHERE SKILL_CODE &(
    select sum(code)
    from skillcodes
    where category = "Front End"
    )
ORDER BY ID