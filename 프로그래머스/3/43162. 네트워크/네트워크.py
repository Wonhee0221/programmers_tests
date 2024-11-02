from collections import deque
def BFS(n,computers, i, visited):
    visited[i] = True
    que = deque()
    que.append(i)
    while que:
        i = que.popleft()
        visited[i] = True
        for x in range(n):
            if x != i and computers[i][x] == 1:
                if visited[x] == False:
                    que.append(x)
    
def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if visited[i] == False:
            answer += 1
            BFS(n,computers, i,visited)
    return answer