import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

while True:
  y, x = map(int,input().split())
  if x == 0 and y == 0:
    break
  graph = []
  cnt = 0
  visited = [[False] * y for _ in range(x)]

  def dfs(i,j):
    visited[i][j] = True
    dx, dy = [0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,-1,1]
    for d in range(8):
      nx = i+dx[d]
      ny = j+dy[d]
      if 0 <= nx < x and 0 <= ny < y:
        if graph[nx][ny] == 1 and not visited[nx][ny]:
          dfs(nx,ny)

  for d in range(x):
    list_s = list(map(int,input().split()))
    graph.append(list_s)
  for i in range(x):
    for j in range(y):
      if graph[i][j] == 1 and not visited[i][j]:
        dfs(i,j)
        cnt += 1
  print(cnt)

