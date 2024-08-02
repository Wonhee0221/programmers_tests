def solution(A, B):
    if A == B:
        return 0
    for turn in range(len(A)):
        A = A[-1] + A[:-1]
        if A == B:
            return turn+1
    answer = -1
    return answer