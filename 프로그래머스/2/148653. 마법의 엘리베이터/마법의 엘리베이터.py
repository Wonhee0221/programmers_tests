# def solution(storey):
#     stack = [int(x) for x in str(storey)]
#     answer = 0

#     for i in range(len(stack)):
#         x = stack.pop()
#         if x > 5:
#             answer += (10 - x)
#             if stack:
#                 stack[-1] += 1
#         else:
#             answer += x

#     return answer


def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer