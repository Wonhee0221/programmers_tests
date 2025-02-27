import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


# 처음엔 테스트 갯수 주어짐
t = int(input())

for _ in range(t):
  answer = 0
  #맵의 크기, 배추수
  n,m,beachu = map(int,input().split())
  # 맵
  graph = [[0]*m for _ in range(n)]
  # 상하좌우
  go = [(0,1),(0,-1),(1,0),(-1,0)]

  for _ in range(beachu):
    x,y = map(int,input().split())
    graph[x][y] = 1
  
  def dfs(x,y):
    visited[x][y] = True
    for dx,dy in go:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        if not visited[nx][ny]:
          dfs(nx,ny)

  visited = [[False]*m for _ in range(n)]

  for x in range(n):
    for y in range(m):
      if graph[x][y] == 1 and not visited[x][y]:
        dfs(x,y)
        answer += 1

  print(answer)



