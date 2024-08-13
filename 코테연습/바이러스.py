
n=int(input()) # 컴퓨터 개수
m=int(input()) # 연결선 개수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 연결된 컴퓨터의 정보가 언제가 1부터 등장한다는 보장 x
    graph[a].append(b)
    graph[b].append(a)
print(graph)
visited =  [[]*(n+1) for _ in range(n+1)]
cnt = 0
def DFS(virus):
    global cnt
    visited[virus]=1
    for i in graph[virus]:
        if (visited[i]==0):
            DFS(i)
            cnt+=1
    return cnt   

print(DFS(1))


