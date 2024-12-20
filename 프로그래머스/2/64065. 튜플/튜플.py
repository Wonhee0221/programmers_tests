def solution(s):
    answer = []
    s = sorted(s[2:-2].split("},{"), key=len)
    for i in s:
        i2 = i.split(",")
        for x in i2:
            if not int(x) in answer:
                answer.append(int(x))
    return answer