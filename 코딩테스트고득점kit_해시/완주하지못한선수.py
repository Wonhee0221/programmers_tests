#코딩테스트 고득점 kit/해시/revel1(완주하지못한선수)
def solution(participant, completion):
    answer = ''
    for i in participant:
        if i in completion:
            completion.remove(i)
            continue
        else:
            answer = i
    return answer

#other
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer