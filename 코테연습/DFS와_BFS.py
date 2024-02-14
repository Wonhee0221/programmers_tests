# https://www.acmicpc.net/problem/1260
from collections import deque
# n,m,v = map(int,input().split())
n,m,v = 4,5,1
# node =[[999, 1000]]
node = [
[1, 2],
[1, 3],
[1, 4],
[2, 4],
[3, 4]]
# n,m,v =5, 5, 3


# node = [
# [5 ,4],
# [5 ,2],
# [1, 2],
# [3 ,4],
# [3, 1]]

visited = []
def dfs(node, v, visited):
  visited.append(v)
  print(v,end=' ')
  for i in node:
    if v in i: 
      for x in i:
        if x not in visited:
          dfs(node,x,visited)

dfs(node,v,visited)
print("")

# n,m,v =4,5,1
# # n,m,v =1000 ,1 ,1000

# node = [
# [1, 2],
# [1, 3],
# [1, 4],
# [2, 4],
# [3, 4]]
# # node = [
# # [999, 1000]
# # ]

# visited=[]

# def bfs(node, v, visited):
#   queue = deque([v])
#   visited.append(v)
#   while queue:
#     x = queue.popleft()
#     print(x,end=' ')
#     for i in node:
#       if x in i:
#         for q in i:
#           if q not in visited:
#             queue.append(q)
#             visited.append(q)
        
# bfs(node,v,visited)

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

