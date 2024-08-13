import sys

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

buket = {i:0 for i in range(1,n+1)}
for x in arr:
    i,j,k = x
    for first in range(i,j+1):
        for number in range(1,k+1):
            buket[first] = number
answer = list(buket.values())
for a in answer:
    print(a,end=" ")