import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
cnt = int(input())
net = [[] for _ in range(num+1)]
for x in range(cnt):
  i,j = map(int,input().split())
  net[i].append(j)
  net[j].append(i)

count = 0
que = deque()
que.append(1)
visited = [False for _ in range(num+1)]
while que:
  start = que.popleft()
  visited[start] = True
  for i in net[start]:
    if not visited[i]:
      que.append(i)
      visited[i] = True
      count += 1 

print(count)