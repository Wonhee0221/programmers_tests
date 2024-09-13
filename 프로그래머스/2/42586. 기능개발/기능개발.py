def solution(progresses, speeds):
    answer = []
    day = 0 
    cnt = 0 
    while progresses:
        day += 1
        while progresses and progresses[0] + day * speeds[0] >= 100:
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
            
    return answer
