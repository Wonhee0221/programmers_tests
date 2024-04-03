from collections import deque

def solution(priorities, location):
    x =  [(i,p) for i,p in enumerate(priorities)]
    bin_queue = deque(x)
    answer = 0
    while bin_queue:
        cur = bin_queue.popleft()
        if any(cur[1] < q[1] for q in bin_queue):
            bin_queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
        