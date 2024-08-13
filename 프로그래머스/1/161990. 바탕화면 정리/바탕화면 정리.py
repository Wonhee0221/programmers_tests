def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    max_x, max_y = 0, 0
    min_x, min_y = n+1, m+1
    
    for i in range(n):
        for y in range(m):
            if wallpaper[i][y] == "#":
                if i < min_x:
                    min_x = i
                if y < min_y:
                    min_y = y
                if i > max_x:
                    max_x = i
                if y > max_y:
                    max_y = y
                
    answer = [min_x, min_y,max_x+1, max_y+1]
    return answer