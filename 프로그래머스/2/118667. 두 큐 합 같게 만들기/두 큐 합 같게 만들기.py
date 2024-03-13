from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    count = 0
    for i in range(len(q1)*3):
        if sum1 == sum2:
            return count;
        elif sum1 > sum2:
            x = q1.popleft()
            q2.append(x)
            sum1 -=x
            sum2 +=x
            count+=1
            if sum1 == sum2:
                return count;
                break;
        elif sum1 < sum2:
            x = q2.popleft()
            q1.append(x)
            count+=1
            sum1+=x
            sum2-=x
            if sum1 == sum2:
                return count;
                break;
    return -1
# from collections import deque
# def solution(queue1, queue2):
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     q1
#     count = 0
#     for i in range(len(q1)*3):
#         if sum(q1) > sum(q2):
#             x = q1.popleft()
#             q2.append(x)
#             count+=1
#             if sum(q1) == sum(q2):
#                 return count
#         elif sum(q1) < sum(q2):
#             x = q2.popleft()
#             q1.append(x)
#             count+=1
#             if sum(q1) == sum(q2):
#                 return count
#         else:
#             return count
#     return -1