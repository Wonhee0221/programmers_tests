"""
아이디어
1. 먼저 K 개의 답을 구한다음 
2. for 문으로 다음인덱스 값을 더하고, 앞의 값을 빼면 된다.
3. 이때 최대값 갱신

시간복잡도
O(N)

자료구조
전체 배열 : int[]
카운트 : int
"""

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
gre = list(map(int,input().split()))
start = sum(gre[:K])
max_num = start
for x in range(K,N):
  start -= gre[x-K]
  start += gre[x]
  max_num = max(max_num, start)
print(max_num)