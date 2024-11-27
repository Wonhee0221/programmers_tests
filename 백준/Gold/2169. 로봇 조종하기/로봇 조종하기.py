import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dp = []
for i in range(N):
  dp.append(list(map(int,input().split())))
for i in range(1,M):
  dp[0][i] += dp[0][i-1]
for i in range(1,N):
  dpl = dp[i][:]
  dpr = dp[i][:]
  for j in range(M):
    if j == 0:
      dpl[j] += dp[i-1][j]
      dpr[M-1-j] += dp[i-1][M-1-j]
    else:
      dpl[j] += max(dp[i-1][j],dpl[j-1])
      dpr[M-1-j] += max(dp[i-1][M-1-j],dpr[M-j])
  for j in range(M):
    dp[i][j] = max(dpl[j],dpr[j])
print(dp[-1][-1])