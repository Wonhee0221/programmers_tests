from collections import Counter
def solution(points, routes):
    answer = 0
    target = []
    for route in routes:
        idx= 0
        for i in range(len(route) - 1):
            sx, sy = points[route[i] - 1]
            ex, ey = points[route[i + 1] - 1]

            # x 좌표 맞추기
            while sx != ex:
                target.append((sx, sy, idx))
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                idx += 1

            # y 좌표 맞추기
            while sy != ey:
                target.append((sx, sy, idx))
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                idx += 1
        target.append((sx, sy, idx))
    # 체크
    counts = Counter(target)
    for i in counts.values():
        if i >= 2:
            answer +=1 
        
    return answer

