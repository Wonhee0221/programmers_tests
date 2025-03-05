import sys
input = sys.stdin.readline

word_list = set()
dx,dy = [0,0,1,-1],[1,-1,0,0]
def dfs(x,y, sixword):
  if len(sixword) == 6:
    word_list.add(sixword)
    return
  for c in range(4):
    nx = x + dx[c]
    ny = y + dy[c]
    if 0 <= nx < 5 and 0 <= ny < 5:
        dfs(nx, ny, sixword + str(graph[nx][ny]))

graph = []
for x in range(5):
  maps = list(map(int,input().split()))
  graph.append(maps)


for x in range(5):
  for y in range(5):
    dfs(x,y,str(graph[x][y]))

print(len(word_list))