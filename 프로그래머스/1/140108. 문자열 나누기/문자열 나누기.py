def solution(s):
    one = 0
    two = 0
    answer = 0
    for i in s:
        if one == two:
            answer+=1
            k=i
        if k == i:
            one+=1
        else:
            two+=1
        
    return answer