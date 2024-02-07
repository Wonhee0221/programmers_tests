def solution(n, times):
    answer = 0
    times.sort()
    
    start = times[0]
    end = times[-1] * n
    
    while start <= end:
        mid = (start+end)//2
        print(mid)
        
        capacity = 0
        
        for t in times:
            capacity +=mid//t
        # print(capacity)

        if capacity >= n:
            answer = mid
            end = mid - 1

        else:
            start = mid + 1
    return answer
n=6
times	=[7, 10]
solution(n,times)