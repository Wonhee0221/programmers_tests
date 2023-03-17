def solution(sides):
    cnt=0
    answer = sum(sides)
    for i in range(max(sides)-min(sides),max(sides)):
        cnt+=1
    for x in range(max(sides),answer-1):
        cnt+=1
    return cnt

solution([3,6])