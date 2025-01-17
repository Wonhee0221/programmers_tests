import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open("./백준/입력창메모/5014_스타트링크_input.txt", "r") 
F, S, G, U, D = map(int,input().split())

visited =  [0 for _ in range(F + 1)]  

def bfs():
  que = deque()
  que.append(S)
  visited[S] = 1
  while que:
    start = que.popleft()
    if start == G:
      return visited[start] - 1
    for i in (start + U, start-D):
      if (0< i <= F) and visited[i] == 0:
        visited[i] = visited[start] + 1
        que.append(i)
  return("use the stairs")
print(bfs())