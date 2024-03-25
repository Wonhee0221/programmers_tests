from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    start = [0,0]
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] !=0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx,ny])
                    print(maps[nx][ny])
                    
    return -1 if maps[n-1][m-1] == 1 else maps[n-1][m-1]