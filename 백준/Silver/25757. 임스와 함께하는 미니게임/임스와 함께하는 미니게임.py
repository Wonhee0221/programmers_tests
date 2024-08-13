game = {"Y":1,"F":2,"O":3}
played = set()
n,m = input().split()
n = int(n)
cnt = game[m]
for i in range(n):
  name = input()
  played.add(name)
print(len(played)//cnt)