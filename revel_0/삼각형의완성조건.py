def solution(sides):
    x = max(sides)
    sides.remove(x)
    print(sides, x)
    if sides[0]+sides[1] < x or sides[0]+sides[1] == x:
        return 2
    else:
        return 1
    
print(solution([3, 6, 2]))