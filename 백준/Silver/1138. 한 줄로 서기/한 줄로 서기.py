import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int,input().split()))
answer = [0] * n
for i in range(n):
  t = order[i]
  cnt = 0
  for p in range(n):
    if cnt == t and answer[p] == 0:
      answer[p] = i+1
      break
    elif answer[p] == 0:
        cnt += 1
# for i in answer:
#   print(i, end= " ")
print(*answer)
