import sys
input = sys.stdin.readline

N = int(input())

DP= [0] * 12
DP[1] = 1
DP[2] = 2
DP[3] = 4

for i in range(N):
  num = int(input())
  for i in range(4,num+1):
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]
  print(DP[num])