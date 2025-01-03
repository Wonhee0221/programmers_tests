
def solution(plans):
    answer = []
    for i in range(len(plans)):
        h,m = map(int,plans[i][1].split(":"))
        plans[i][1] = h* 60+m
        plans[i][2] = int(plans[i][2])
    # 정렬
    plans = sorted(plans, key = lambda x:x[1])
    stack = []
    for t in range(len(plans)):
        if t == len(plans) - 1:
            stack.append(plans[t])
            break
        
        name, start, time = plans[t]
        
        if (start+time) > plans[t+1][1]:
            plans[t][2] =  time - (plans[t+1][1] - start)
            stack.append(plans[t])
        else:
            answer.append(name)
            #남은시간 구하기
            use_time = plans[t+1][1] - (start+time)
            # 남은시간 가지고 노는데 스택에 남은게 있고 남은시간도 있으면
            while use_time != 0 and stack:
                uname, ustart, utime = stack.pop()
                # 만약 남은 시간보다 스택에 있는 남은 시간이 크면, 즉 스택 시간이 적으면
                if use_time >= utime:
                    answer.append(uname)
                    use_time -= utime
                else:
                    stack.append([uname, ustart, utime-use_time])
                    use_time = 0
                
    while stack:
        n, st, t = stack.pop()
        answer.append(n)
    
    
    return answer