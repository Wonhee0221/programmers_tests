from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    largest_number = (max(max(sublist) for sublist in rectangle) + 1) * 2
    maps = [[-1]*largest_number for _ in range(largest_number)]
    answer = 0
    for i in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, i)
        for x in range(x1,x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    maps[x][y] = 0
                elif maps[x][y] != 0:
                    maps[x][y] =1
    # 길찾기
    que = deque()
    que.append([characterX*2, characterY*2,0])
    visited = [[0]*largest_number for _ in range(largest_number)]
    visited[characterX * 2][characterY * 2] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while que:
        x,y,cnt = que.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = cnt//2
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < largest_number and 0 <= ny < largest_number:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    que.append([nx,ny,cnt+1])
                    visited[nx][ny] = 1
    return answer