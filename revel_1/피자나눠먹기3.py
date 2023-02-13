def solution(slice, n):
    cnt = 1
    add=slice
    while(slice // n != 1):
        slice +=add
        cnt += 1
    return cnt

print(solution(10, 1))


#코드 실수
# def solution(slice, n):
#     cnt = 1
#     while(slice // n != 1):
#         slice = slice*2
#         cnt += 1
#     return cnt

# print(solution(4, 16))


#이러면 안되는게 *2를 해버리면 조각씩 증가해야하는데 배수로 증가하기때문에 오류가남.

#다른답안
def solution(slice, n):
    return ((n - 1) // slice) + 1
