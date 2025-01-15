import sys
from collections import deque
input = sys.stdin.readline

# m, n, h
m, n, h = map(int,input().split())
graph = [[] for _ in range(h)]
for i in range(h):
  for j in range(n):
    graph[i].append(list(map(int,input().split())))

# 방향
go = [[-1,0,0],[1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1],]

def bfs():
    while que:
        curr_h, curr_row, curr_col = que.popleft()
        for direction in range(6):
            delta_h, delta_row, delta_col = go[direction]
            next_h = curr_h + delta_h
            next_row = curr_row + delta_row
            next_col = curr_col + delta_col
            if 0 <= next_h < h and 0 <= next_row < n and 0 <= next_col < m:
                if graph[next_h][next_row][next_col] == 0:
                    que.append((next_h, next_row, next_col))
                    graph[next_h][next_row][next_col] = graph[curr_h][curr_row][curr_col] + 1



que = deque()

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        que.append((i,j,k))

bfs()

        
unsuccess = False
day = 0

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 0:
        unsuccess = True
      day = max(day, graph[i][j][k])
if unsuccess:
  print(-1)
else:
  print(day-1)