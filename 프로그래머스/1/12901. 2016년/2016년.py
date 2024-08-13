def solution(a, b):
    day = -1
    for i in range(1,a):
        if i in (1,3,5,7,8,10,12):
            day += 31
        elif i == 2:
            day+=29
        else:
            day += 30
    
    day+=b
    week = ["FRI","SAT","SUN","MON",'TUE','WED',"THU"]
    x = day%7
    return week[x]