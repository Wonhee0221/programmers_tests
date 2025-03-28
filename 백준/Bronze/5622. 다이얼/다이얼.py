import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

word = input().strip()

def alpha_num(i):
  if i in ["A","B","C"]:
    return 3
  elif i in ["D","E","F"]:
    return 4
  elif i in ["G","H","I"]:
    return 5
  elif i in ["J","K","L"]:
    return 6
  elif i in ["N","M","O"]:
    return 7
  elif i in ["P","Q","R","S"]:
    return 8
  elif i in ["T","U","V"]:
    return 9
  elif i in ["W","X","Y","Z"]:
    return 10
  else:
    return 0

result = 0
for i in word:
  result += alpha_num(i)
print(result)