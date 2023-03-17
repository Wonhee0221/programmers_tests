# 프로그래머스 코딩테스트 연습, 코딩테스트 입문, 옹알이(1) 파이썬풀이
x =["ayaye", "uuuma", "ye", "yemawoo", "ayaa","yemaye"]


def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    for utter in babbling: #주어지는거 맨처음부터 알아보기.
        for text in babble: #할수 있는말 맨처음부터 비교하기.
            if text * 2 not in utter: # 한단어당 1번밖에 사용이 불가능하기 때문에 *2를 써서 2개 들어간것을 방지.
                utter = utter.replace(text, ' ',1) #텍스트단어를 스페이스으로 대체,그리고 그 횟수는 1번만 들어가야하기 때문에 1을 추가해줌.
        if utter.strip() == '': #그리고 스페이스인경우 strip()을통해 공란으로 만든후 만약 공란일 경우 카운트에 추가
            count += 1
    return count

# ☝조카가 가능한 네 가지 발음이 담긴 배열을 만들어 줍니다.
# ✌입력값으로 들어온 babbling 배열을 for문을 돌리며, 조카가 가능한 네 가지 발음이 담긴 babble배열과 비교할 것입니다.
# 🤞이 때 연속된 발음이 들어있지 않다면, 조카가 가능한 발음과 일치하는 부분을 모두 공백으로 바꿔줍니다.
# 🖖전 단계 과정을 거친 단어가 공백을 제외하고 아무것도 없다면 조카가 발음할 수 있는 단어이기에 count를 추가해줍니다.
print(solution(x))