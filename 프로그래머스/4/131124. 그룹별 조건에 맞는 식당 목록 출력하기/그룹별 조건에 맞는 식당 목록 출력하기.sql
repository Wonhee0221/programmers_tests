-- 코드를 입력하세요
-- 출력 : 회원이름, 리뷰 텍스트, 리뷰작성일
-- 정렬 : 리뷰작성일 기준 ASC, 리뷰 텍스트 ASC
-- join조건 : MEMBER_ID
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") as REVIEW_DATE
FROM MEMBER_PROFILE M join REST_REVIEW R on M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID = (
SELECT MEMBER_ID
FROM REST_REVIEW
Group by MEMBER_ID
order by count(*) desc
limit 1)
order by REVIEW_DATE ASC, REVIEW_TEXT ASC