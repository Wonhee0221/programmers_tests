from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(c, node, visited):
  queue = deque()
  queue.append([c])
  visited[c] = True
  while queue:
    x = queue.popleft()
    for r in node[x]:
      if visited[r] == False:
        visited[r] = True
        queue.append(r)

n, m = map(int, input().split())
node = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
cnt =0
visited = [False] * (n+1)
for c in range(1,n+1):
  if visited[c]==False:
    bfs(c,node,visited)
    cnt += 1 
print(cnt)
