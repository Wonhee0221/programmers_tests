def solution(arr1, arr2):
    answer = []
    # 전체리스트 돌기
    for i in range(len(arr1)):
        new = []
        for x in range(len(arr2[0])): # 이게 저장할 리스트 도는거 1, 2,3
            new_x= 0
            for t in range(len(arr2)):
                new_x += arr1[i][t] * arr2[t][x]
            new.append(new_x)
        answer.append(new)
    return answer
