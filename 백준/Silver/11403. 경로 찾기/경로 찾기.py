import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
for x in range(n):
  gl = list(map(int,input().split()))
  for t in range(n):
    if gl[t] == 1:
      graph[x].append(t)

def bfs():
  visited = [False] * n
  que = deque()
  for cg in graph[answer]:
    que.append(cg)
  while que:
    y = que.popleft()
    if not visited[y]:
      visited[y] = True
      for cf in graph[y]:
        que.append(cf)
  return visited

for answer in range(n):
  list_g = bfs()
  for x in list_g:
    if x == True:
      print(1, end=" ")
    else:
      print(0, end=" ")
  print()
  