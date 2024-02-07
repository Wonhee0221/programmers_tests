def solution(genres, plays):
    dict_categore = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] in dict_categore :
            dict_categore[genres[i]][0] += plays[i]
            dict_categore[genres[i]][1] += [[i,plays[i]]]
            # print(dict_categore[genres[i]][0])
        else:
            dict_categore[genres[i]] =  [plays[i],[[i,plays[i]]]]
            print(dict_categore)
    rank = list(sorted(dict_categore.items(), key= lambda x :x[1][0], reverse=True))
    print(dict_categore[rank[0][0]])
    # for r in range(len(rank)):
    #     test = sorted(dict_categore[rank[r][0]], key= lambda x :(int(x[1]), int(-x[0])), reverse=True)
    #     if len(test) == 1:
    #         answer.append(test[0][0])
    #         print(test)
    #     else:
    #       [answer.append(i[0]) for i in test[:2]]
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop", "R&B"],[500, 600, 500, 800, 2500,6000]) )