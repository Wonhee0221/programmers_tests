from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    column_oil = [0] * m  # 각 열에서 캘 수 있는 최대 석유량

    def bfs(start_y, start_x):
        queue = deque([(start_y, start_x)])
        visited[start_y][start_x] = True
        count = 1
        columns = set([start_x])  # 이 덩어리가 포함된 열들을 저장

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            y, x = queue.popleft()
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and land[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    count += 1
                    columns.add(nx)

        return count, columns

    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and not visited[y][x]:
                oil_size, columns = bfs(y, x)
                for col in columns:
                    column_oil[col] += oil_size

    return max(column_oil)
