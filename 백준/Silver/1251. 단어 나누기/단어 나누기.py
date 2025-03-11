import sys
input = sys.stdin.readline

n = input().strip()
min_str = "z" * len(n)
for i in range(1,len(n)-1):
  for j in range(i+1,len(n)):
    new_str = n[:i][::-1]+n[i:j][::-1]+n[j:][::-1]
    min_str = min(min_str,new_str)
print(min_str)