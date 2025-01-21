import sys
input = sys.stdin.readline
from collections import deque



def bfs():
    m = int(input())
    pan = [[0]*m for _ in range(m)]
    visited = [[False]*m for _ in range(m)]
    que = deque()
    start = list(map(int,input().split()))
    end = list(map(int,input().split()))
    que.append(start)
    visited[start[0]][start[1]]
    while que:
        x, y = que.popleft()
        if [x, y] == end:
            return 0
        for dx,dy in night:
            nx = x + dx
            ny = y + dy
            if [nx,ny] == end:
                return pan[x][y] + 1
            if 0 <= nx < m and 0<= ny < m :
                if not visited[nx][ny]:
                    que.append([nx,ny])
                    visited[nx][ny] = True
                    pan[nx][ny] = pan[x][y] + 1

n = int(input())
night = [(1,2),(-1,2),(-1,-2),(1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]
for x in range(n):
    print(bfs())
    


