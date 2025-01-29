import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    answer = ''
    num, words = input().split()
    for x in words:
        answer += x*int(num)
    print(answer)
        
