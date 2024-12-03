import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  listcol = int(input())
  DP = [list(map(int,input().split())) for _ in range(2)]

  if listcol > 1:
      DP[0][1] += DP[1][0]
      DP[1][1] += DP[0][0]
  for i in range(2,listcol):
      DP[0][i] += max(DP[1][i-2],DP[1][i-1])
      DP[1][i] += max(DP[0][i-1],DP[0][i-2])
    
  print(max(DP[0][listcol-1],DP[1][listcol-1]))