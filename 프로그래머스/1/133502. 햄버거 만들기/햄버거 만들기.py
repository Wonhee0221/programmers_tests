def solution(ingredient):
    answer = 0
    ff = []
    cnt = 0
    for i in range(len(ingredient)):
        ff.append(ingredient[i])
        if (len(ff) > 3 and ff[-4:]==[1,2,3,1]):
            answer +=1
            ff.pop()
            ff.pop()
            ff.pop()
            ff.pop()
    return answer

    # while cnt<len(ingredient):
    #     if ingredient[cnt:cnt+4] == [1,2,3,1]:
    #         del ingredient[cnt:cnt+4]
    #         print(ingredient)
    #         answer+=1
    #         cnt=cnt-3
    #     cnt+=1