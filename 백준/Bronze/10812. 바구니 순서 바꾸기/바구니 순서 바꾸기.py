import sys
input = sys.stdin.readline
n,m  = map(int,input().split())
num = [x for x in range(1,n+1)]

for t in range(m):
  i,j,k = map(int,input().split())
  num[i-1:j] = num[k-1:j] + num[i-1:k-1]

for word in num:
  print(word,end=" ")