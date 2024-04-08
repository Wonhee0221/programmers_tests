import heapq
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville)
    while len(scoville) >=2:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer
        else:
            min2 = heapq.heappop(scoville)
            new = min1 + min2 *2
            heapq.heappush(scoville, new)
            answer+=1
    if scoville[0]>=K:
        return answer
    else:
        return -1
            