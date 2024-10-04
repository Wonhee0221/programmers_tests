def solution(storey):
    answer = 0
    while storey:
        na = storey % 10
        if na > 5:
            answer += (10 - na)
            storey += 10
        elif na < 5:
            answer += na
        else:
            if (storey//10) % 10 > 4:
                storey += 10
            answer += 5
        storey = storey // 10
    return answer