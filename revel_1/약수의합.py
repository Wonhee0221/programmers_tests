#코딩테스트 연습/revel_1/약수의합.

#내 풀이
def solution(n):
    answer = [n]
    for i in range(1,n//2+1):
        if n % i == 0:
            answer.append(i)
    return sum(answer)

#다른사람풀이
def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상된다.
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

#항상 리스트 컴프리헨션을 잘 쓰면 좋다는 생각을 매번하지만
#사용할줄 몰라서 못쓴다...나도 잘하고싶다...
