"""
1.아이디어
- 점화식을 떠올린다.
- 1일때 1 2일때 2 3일때 3 4일때 6이다 그럼
- N = N-2 + N-1 이라는 식이 성립.
- 마지막 답은 10007로 나눈 나머지 출력
2.시간복잡도
- O(N)
3.자료구조
N의 크기 : int
방법의 수 = int
"""
import sys
input = sys.stdin.readline
N = int(input())
rs = [0,1,2]
for i in range(3,N+1):
  rs.append((rs[i-1]+rs[i-2])%10007)

print(rs[N])