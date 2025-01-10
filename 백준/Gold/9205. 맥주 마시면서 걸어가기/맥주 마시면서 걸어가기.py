import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  x,y = map(int,input().split()) # 출발지
  stores = [tuple(map(int, input().split())) for _ in range(n)]  # 편의점 좌표
  tar, get = map(int,input().split())
  que = deque([(x,y)]) # 출발지
  visited = set()
  answer = False
  while que:
    p_x, p_y = que.popleft()
    if abs(p_x - tar) + abs(p_y - get) <= 1000:
      answer = True
      break
    for i in range(len(stores)):
      if i not in visited and abs(p_x - stores[i][0]) + abs(p_y- stores[i][1]) <= 1000:
        visited.add(i)
        que.append((stores[i][0],stores[i][1]))
  print("happy" if answer else "sad")
  
