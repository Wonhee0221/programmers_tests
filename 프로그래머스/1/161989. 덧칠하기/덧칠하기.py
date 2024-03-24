def solution(n, m, section):
    answer = 1
    p = section[0]
    for i in section:
        if i-p >= m:
            p = i
            answer += 1
    return answer




# def solution(n, m, section):
#     answer = 0
#     x =[0 if i in section else i for i in range(1,n+1) ]
#     index = section[0]-1
#     while index < n:
#         if x[index] == 0:
#             answer += 1
#             index += m
#         else:
#             index+=1
#     return answer


