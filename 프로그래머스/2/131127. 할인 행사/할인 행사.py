def solution(want, number, discount):
    date = 0
    answer = 0
    while date+10 <= len(discount):
        want_dict = dict(zip(want, number))
        for i in range(date, date+10):
            if discount[i] in want_dict and want_dict[discount[i]] >0:
                want_dict[discount[i]] -= 1
        date += 1
        if sum(want_dict.values()) == 0:
            answer +=1

    return answer