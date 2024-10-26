"""
1) 아이디어
- N개의 정수  A[N]이 주어진다 여기서 X라는정수가?
- 일단 무조건 N 개보다 큰수가 들어오면 OUT
- 그리고 N과 M이 100,000개 이기때문에 O(N*M) 하기는 불가
2) 시간 복잡도
- 이진탐색 - O(logN)
3) 자료구조
가장 큰수 N : int
답지 리스트 : int[][]
정답 리스트 : int[][]
"""
import sys
input = sys.stdin.readline
N = int(input())
answer_list = list(map(int,input().split()))
answer_list.sort()
M = int(input())
search_list = list(map(int,input().split()))

def search(st, en, target):
  if st == en:
    if answer_list[st] == target:
      print(1)
    else:
      print(0)
    return
  mid = (st+en)//2
  if answer_list[mid] < target:
    search(mid+1,en,target)
  else:
    search(st, mid, target)
for x in search_list:
    search(0,N-1,x)