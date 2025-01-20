import sys
import heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    num = int(input())
    if 0 < num:
        heapq.heappush(q,num)
    else:
        if q:
            t = heapq.heappop(q)
            print(t)
        else:
            print(0)
