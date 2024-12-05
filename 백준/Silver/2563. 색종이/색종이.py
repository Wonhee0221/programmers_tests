import sys
input = sys.stdin.readline
'''
3
3 7
15 7
5 2
'''
n = int(input())
map_list = [[0] *101 for _ in range(100+1)]
for _ in range(n):
  x,y = map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      map_list[i][j] = 1
answer = 0
for x in range(101):
  answer += sum(map_list[x])
print(answer)