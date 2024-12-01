import sys
input = sys.stdin.readline

num = int(input())
st = [0] * 301
for i in range(1, num + 1):
  st[i] = int(input())

dp = [0] * 301

dp[1] = st[1]
dp[2] = st[1] + st[2]
dp[3] = max(st[3]+st[1],st[3]+st[2])

for i in range(4,num+1):
  dp[i] = max(dp[i-3]+st[i-1] + st[i], dp[i-2]+st[i])

print(dp[num])