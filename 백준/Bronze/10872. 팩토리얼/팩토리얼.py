num = int(input())
answer = 1
if num == 0:
  print(answer)
else:
  for i in range(1,num+1):
    answer *=i
  print(answer)