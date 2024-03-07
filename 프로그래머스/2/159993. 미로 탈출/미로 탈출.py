from collections import deque

def bfs(start, end, maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False]*m for _ in range(n)]
    que = deque()
    
#     시작 지점 찾기
    for i in range(n):
        for c in range(m):
            if maps[i][c] == start:
                visited[i][c] = True
                que.append((i,c,0))
                break;
                
    while que:
        y, x, cost = que.popleft()
        
        if maps[y][x] == end:
            return cost
        
        for l in range(4):
            ny = y + dy[l]
            nx = x + dx[l]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X":
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((ny,nx,cost+1))
    return -1
                
def solution(maps):
    first = bfs("S","L",maps)
    final = bfs("L","E",maps)
    if first != -1 and final != -1:
        return first + final
    return -1