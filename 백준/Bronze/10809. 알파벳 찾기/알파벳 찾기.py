import sys
input = sys.stdin.readline

s = input()

for i in range(ord("a"),ord("z")+1):
  check = True
  for x in range(len(s)):
    if i == ord(s[x]):
      print(x,end=" ")
      check = False
      break
  if check:
    print(-1,end=" ")
