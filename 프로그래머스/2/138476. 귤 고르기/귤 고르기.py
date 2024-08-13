def solution(k, tangerine):
    x={}
    answer = 0
    for i in tangerine:
        if i in x:
            x[i]+=1
        else:
            x[i]=1
    c= dict(sorted(x.items(), key=lambda x:x[1], reverse=True))
    for i in c:
        if k<=0:
            return answer
        k-=c[i]
        answer+=1

    return answer