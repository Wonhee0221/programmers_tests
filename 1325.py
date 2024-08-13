import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
real = []
max_cnt = 0
computer = [[] for _ in range(n)]

for i in range(m):
    x,y = list(map(int,input().split()))
    computer[y-1].append(x)


def bfs(index):
    sum = 0
    que = deque([index])
    visited = [False] *(n+1)
    visited[index+1] =True
    while que:
        now = que.popleft()
        for next in computer[now]:
            if not visited[next]:
                que.append(next-1)
                visited[next] = True
                sum += 1
    return sum

result = 0
for t in range(n):
    result = bfs(t)
    if result > max_cnt:
        max_cnt = result
        real=[t+1]
    elif result == max_cnt:
        real.append(t+1)    
print(*real)