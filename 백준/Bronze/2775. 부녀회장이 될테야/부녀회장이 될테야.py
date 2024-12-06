import sys 
inpurt = sys.stdin.readline


n = int(input())
for x in range(n):
  k = int(input())
  num = int(input())
  zero_F = [t for t in range(1,num+1)]
  for c in range(k):
    for i in range(1, num):
      zero_F[i] += zero_F[i-1]
  print(zero_F[-1])

 
