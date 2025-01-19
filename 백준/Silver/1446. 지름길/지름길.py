import sys
input = sys.stdin.readline

n, d = map(int,input().split())

distance = []
for x in range(n):
    s, e, l = map(int, input().split())
    if e > d or e - s < l:
        continue
    distance.append([s, e, l])
distance.sort(key=lambda x: (x[0], x[1]))

# DP 배열 초기화
dp = [i for i in range(d + 1)]  # dp[i]: 0부터 i까지의 최소 거리

# DP 계산
for s, e, l in distance:
    dp[e] = min(dp[e], dp[s] + l)  # 지름길을 사용하는 경우
    for i in range(s + 1, d + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)  # 지름길 외의 일반 도로

# 결과 출력
print(dp[d])