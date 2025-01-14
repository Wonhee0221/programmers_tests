import sys
input = sys.stdin.readline

# 출력 
# 심장의 위치, 
# [왼쪽팔, 오른팔, 허리, 왼쪽다리, 오른쪽다리]

# 그래프 길이

n = int(input())
graph = [[False] * n for _ in range(n)]
answer = []

for i in range(n):
    line = str(input().strip())
    for x in range(n):
        if line[x] == "*":
            graph[i][x] = True

# 머리 찾고 심장찾기
head = False
for x in range(n):
    for y in range(n):
        if graph[x][y] == True:
            heart = (x+1, y)
            head = True
            break
    if head:
        break

def mesure(x, y,dx,dy):
    count = 0
    x += dx
    y += dy
    while 0 <= x < n and 0 <= y < n and graph[x][y] == True:
        x += dx
        y += dy
        count += 1
    return count

# 찾기
# 왼쪽팔
left = mesure(heart[0], heart[1], 0, -1)
answer.append(left)
# 오른쪽팔
right = mesure(heart[0], heart[1], 0, 1)
answer.append(right)
#몸통
body_c = mesure(heart[0], heart[1], 1, 0)
body = (heart[0]+body_c, heart[1])
answer.append(body_c)
#왼쪽다리
left_leg = mesure(body[0], body[1]-1, 1, 0)
answer.append(left_leg)
#오른쪽다리
right_leg = mesure(body[0], body[1]+1, 1, 0)
answer.append(right_leg)
print(heart[0]+1, heart[1]+1)
for x in answer:
    print(x, end=" ")