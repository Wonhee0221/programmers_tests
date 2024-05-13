def solution(n, lost, reserve):
    answer = 0
    cnt = []
    lost.sort()
    reserve.sort()
    for x in lost:
        if x in reserve:
            cnt.append(x)
            reserve.remove(x)
            answer+=1
    for i in range(1,n+1):
        if i in cnt:
            continue
        if i in lost:
            if i-1 in reserve:
                answer+=1
                reserve.remove(i-1)
            elif i+1 in reserve:
                answer+=1
                reserve.remove(i+1)
        else:
            answer+=1
    
    return answer