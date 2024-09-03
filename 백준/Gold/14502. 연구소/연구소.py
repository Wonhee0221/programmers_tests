import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 빈 칸(0)의 위치와 바이러스(2)의 위치를 미리 저장
empty = []
virus = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

result = 0

def bfs():
    que = deque(virus)  # 초기 바이러스 위치를 큐에 삽입
    temp_board = [row[:] for row in board]  # 얕은 복사를 사용해 보드를 복사
    
    while que:
        x, y = que.popleft()
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and temp_board[nx][ny] == 0:
                temp_board[nx][ny] = 2
                que.append((nx, ny))

    # 안전 영역 크기 계산
    safe_count = sum(row.count(0) for row in temp_board)
    return safe_count

# 벽을 세울 수 있는 모든 조합에 대해 시뮬레이션
for walls in combinations(empty, 3):
    for x, y in walls:
        board[x][y] = 1
    
    # BFS로 바이러스를 퍼뜨린 후 안전 영역을 계산
    result = max(result, bfs())
    
    for x, y in walls:
        board[x][y] = 0  # 원래 상태로 복원

print(result)
