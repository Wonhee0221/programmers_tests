import sys
from collections import Counter
input = sys.stdin.readline

n = input().strip().upper()
n = Counter(n)
max_word = max(n.values())
max_alpha = [char for char,count in n.items() if count == max_word]
if len(max_alpha)>1:
  print("?")
else:
  print(max_alpha[0])
