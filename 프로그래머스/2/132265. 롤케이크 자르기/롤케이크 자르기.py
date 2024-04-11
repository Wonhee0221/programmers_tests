from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    bro2=set()
    for i in topping:
        bro[i] -= 1
        bro2.add(i)
        if bro[i] ==0:
            bro.pop(i)
        if len(bro) == len(bro2):
            answer+=1
    return answer