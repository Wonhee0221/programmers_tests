"""
1. 아이디어
- 큰 금액의 동전부터 차감
- K를 동전 금액으로 나눈뒤
2. 시간복잡도
N= 10
K = 100,000,000
O(NK) = 10억 OK
3. 자료구조
동전 금액 = int
현재 남은 금액 = int
개수 = int
"""
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
coin_list =[int(input()) for _ in range(N)]
coin_list.reverse()

cnt = 0
for each_coin in coin_list:
  cnt += K//each_coin
  K = K%each_coin
print(cnt)