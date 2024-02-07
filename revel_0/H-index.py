def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)    

    print(citations)
    
    start = 0
    end = len(citations) -1
    
    while start <= end:
        mid  = (start + end)//2
        if citations[mid] >= mid +1:
            answer = start =mid+1
        else:
            end = mid -1 
    return answer


citations=[4,3,1]
print(solution(citations))