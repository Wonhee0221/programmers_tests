import sys
input = sys.stdin.readline

n, l = map(int,input().split())
answer = 0
graph = []
for x in range(n):
    graph.append(list(map(int,input().split())))


def check_going(check_list):
    visited = [False] *n
    for i in range(1,n):
        if abs(check_list[i] - check_list[i-1]) > 1:
            return False
        if (check_list[i-1]-check_list[i]) == 1:
            for x in range(l):
                # 주어진 길이를 넘어가면
                if i+x >= n:
                    return False
                # 밑변을 세울 길이가 다르다면.
                elif check_list[i] != check_list[i+x]:
                    return False
                elif visited[i+x] == True:
                    return False
                elif visited[i+x] == False:
                    visited[i+x] = True
        elif (check_list[i-1]-check_list[i]) == -1:
            for x in range(l):
                if i-1-x < 0:
                    return False
                elif check_list[i-1] != check_list[i-1-x]:
                    return False
                elif visited[i-1-x] == True:
                    return False
                elif visited[i-1-x] == False:
                    visited[i-1-x] = True
    return True


# ## 모든길의 높이가 같다.
for x in range(n):
    if check_going(graph[x]):
        answer += 1
    col = [graph[y][x] for y in range(n)]
    if check_going(col):
        answer += 1

print(answer)
