def solution(m, n, puddles):
    puddles = set((j, i) for i, j in puddles)  # 집합으로 변환
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1,n+1):
        for x in range(1,m+1):
            if i == 1 and x == 1:
                continue
            if (i,x) in puddles:
                graph[i][x] = 0
            else:
                graph[i][x] = (graph[i-1][x] + graph[i][x-1]) % 1000000007
    return graph[n][m] 