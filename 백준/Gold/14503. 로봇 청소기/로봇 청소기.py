"""
아이디어
1. 특정 조건을 만족하는 한 계속 이동 while > for
2. 4방향 먼저 탐색 > 빈칸이 있을경우 이동
3. 4방향 탐색 x > 뒤로 한칸 가서 반복

시간복잡도
O(N*M)

자료구조
전체지도 : int [][]
내위치, 방향 : int(x), int(y), int(d)
카운트 : int
"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
y,x,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]
while True:
  if graph[y][x] == 0:
    graph[y][x] = 2
    cnt += 1
  sw = False
  for i in range(1,5):
    nd = (d - i + 4) % 4
    ny, nx = y + dy[nd], x + dx[nd]
    if 0 <= ny < N and 0 <= nx < M:
      if graph[ny][nx] == 0:
        # 그방향으로 회전한 다음 한칸을 전진하고 1번으로 돌아간다.
        d = nd
        y, x = ny, nx
        sw = True
        break
  # 4방향 모두 있지 않은 경우
  if not sw:
    # 바라보는 방향을 유지한채
    # 뒤쪽 방향이 막혀있는지 확인
    ny = y - dy[d]
    nx = x - dx[d]
    if 0 <= ny < N and 0 <= nx < M:
      if graph[ny][nx] == 1:
        break
      else:
        y = ny
        x = nx
    else:
      break

print(cnt)


