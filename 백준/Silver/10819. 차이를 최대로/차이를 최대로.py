import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
max_num = 0
used = [False] * n

def sum_list(target):
  return sum([abs(target[i]-target[i+1])for i in range(n-1)])

def backtraking(n_list):
  global max_num
  if len(n_list) == n:
    max_num = max(max_num, sum_list(n_list))
    return
  for x in range(n):
    if not used[x]:
      used[x] = True
      backtraking(n_list+[A[x]])
      used[x] = False

backtraking([])
print(max_num)