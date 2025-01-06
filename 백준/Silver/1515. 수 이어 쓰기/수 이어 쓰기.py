import sys
input = sys.stdin.readline

n = input().strip()

cnt = 0
while n:
  cnt += 1
  num = str(cnt)
  for i in num:
    if i == n[0] and n:
      n = n[1:]
      if not n:
        print(num)
        break