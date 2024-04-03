from collections import deque

def solution(priorities, location):
    x = [i for i in range(len(priorities))]
    t= []
    for i in zip(priorities,x):
        t.append(i)
    bin_queue = deque(t)
    stack = []
    answer = 0
    while bin_queue:
        answer+=1
        max_x = max(priorities)
        priorities.remove(max_x)
        loc = bin_queue.popleft()
        if loc[0] == location:
            return 1
        while loc[0] != max_x:
            bin_queue.append(loc)
            loc = bin_queue.popleft()
        if loc[1] == location:
            return answer