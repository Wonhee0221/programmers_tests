"""
3 4 5
3 2
2 2
3 1
2 3
1 1
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,f = map(int,input().split())
graph = [[0]*m for _ in range(n)]
cnt = 0
for _ in range(f):
  x,y = map(int,input().split())
  graph[x-1][y-1] = 1
visited = [[False]*m for _ in range(n)]


def dfs(i,j):
  visited[i][j] = True
  size = 1
  dx, dy = [0,0,1,-1], [1,-1,0,0]
  for x in range(4):
    nx = i+dx[x]
    ny = j+dy[x]
    if 0 <= nx < n and 0<=ny<m and graph[nx][ny] == 1:
      if not visited[nx][ny]:
        size += dfs(nx,ny)
  return size

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      cnt = max(cnt,dfs(i,j))

print(cnt)