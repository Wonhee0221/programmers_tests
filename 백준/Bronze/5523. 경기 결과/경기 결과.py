import sys
input = sys.stdin.readline

n = int(input().strip())
ansa = ansb = 0
for x in range(n):
    a,b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        ansa+=1
    else:
        ansb+=1

print(ansa, ansb)