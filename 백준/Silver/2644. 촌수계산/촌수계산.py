import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tar, get = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for x in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

que = deque([tar])
visited = [False] * (n+1)
res = [0]*(n+1)
while que:
  s = que.popleft()

  visited[s] = True
  for x in graph[s]:
    if not visited[x]:
      que.append(x)
      res[x] = res[s] + 1
      visited[x] = True


print(res[get] if res[get] > 0 else -1)
