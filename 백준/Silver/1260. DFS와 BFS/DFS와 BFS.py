import sys
from collections import deque
input = sys.stdin.readline

n,m,s = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
  x,y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

## 정점 번호가 작은 것 부터 오게 정렬
for i in range(n + 1):
    graph[i].sort()

#DFS
visited = [False] * (n+1)
def DFS(s):
  stack = [s]
  while stack:
    node = stack.pop()
    if not visited[node]:
      visited[node] = True
      print(node, end=" ")
      stack.extend(graph[node][::-1])
      
# BFS
visited1 = [False] * (n+1)
def BFS(s):
  que = deque([s])
  visited1[s] = True
  while que:
    t = que.popleft()
    print(t, end=" ")
    for x in graph[t]:
      if not visited1[x]:
        visited1[x] = True
        que.append(x)

DFS(s)
print()
BFS(s)
