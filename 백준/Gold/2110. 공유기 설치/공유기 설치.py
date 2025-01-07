import sys
input = sys.stdin.readline

n, h = map(int,input().split())
homes = [int(input()) for _ in range(n)] 
homes.sort()
answer = 0

start, end = 1, (homes[-1] - homes[0])

while end >= start:
  mid = (start+end) // 2
  count = 1
  crr = homes[0]

  for x in range(1,n):
    if homes[x] >= crr + mid:
      count +=1 
      crr = homes[x]
      
  if count >= h:
    answer = mid
    start = mid+1
  else:
    end = mid - 1 

print(answer)