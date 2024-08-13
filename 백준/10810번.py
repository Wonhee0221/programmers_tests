# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)

# 도현이는 입력으로 주어진 순서대로 공을 넣는다.

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.
import sys

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

buket = {i:0 for i in range(1,n+1)}
for x in arr:
    i,j,k = x
    for first in range(i,j+1):
        buket[first] = k
answer = list(buket.values())
for a in answer:
    print(a,end=" ")
