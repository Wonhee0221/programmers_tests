import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int,input().split()))
target = int(input())
answer = 0
for x in num_list:
    if x == target:
        answer +=1
print(answer)