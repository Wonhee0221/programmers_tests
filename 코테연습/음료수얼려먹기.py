result =0
n, m = map(int,input().split())
  
def dfs(x,y):
  if x >= n or y>=m or x <= -1 or y <= -1: # 주어진 맵을 벗어나지 않도록.
    return False
  if graph[x][y] == 0: ## 해당 위치가 방문하지 않은 곳이라면
    graph[x][y] = 1 # 방문으로 해주고,
    # 인접 노드들을 찾는다.
    dfs(x-1,y) #좌
    dfs(x,y-1) # 하
    dfs(x+1,y) # 우
    dfs(x,y+1) # 상
    return True 
  return False # 주어진 맵을 넘어가지 않고, 해당 위치의 노드도 방문했을 경우.

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 2차원 리스트이기 때문에 2중 포문을 작성해준다.
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True: #해당 위치의 값을 비교
      result += 1 
print(result)
