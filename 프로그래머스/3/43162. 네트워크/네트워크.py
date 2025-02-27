def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(x):
        visited[x] = True
        for y in range(n):
            if y != x and computers[x][y] == 1 and not visited[y]:
                dfs(y)
    for x in range(n):
        if not visited[x]:
            dfs(x)
            answer += 1
    return answer