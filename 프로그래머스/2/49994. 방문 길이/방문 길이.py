def solution(dirs):
    x,y,visited = 5,5,set()
    graph = [[0]*11 for _ in range(11)]
    graph[x][y] = 1
    go = {"U":[0,-1],"D":[0,1],"L":[-1,0],"R":[1,0]}
    for i in dirs:
        nx = x + go[i][0]
        ny = y + go[i][1]
        if 0 <= nx < 11 and 0 <= ny < 11:
            
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y))
            x = nx
            y = ny
    return len(visited)//2