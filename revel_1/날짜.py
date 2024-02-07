def solution(today, terms, privacies):
    year, month, day = map(int, today.split("."))

    answer = []
    month_dict = {}
    for term in terms:
        case = term[0]
        month_dict[case] = int(term[2:])

    for exam in range(len(privacies)):
        t_year, t_month, t_day = int(privacies[exam][0:4]),int(privacies[exam][5:7]),int(privacies[exam][8:10])
        case = privacies[exam][-1]

        t_month = t_month + month_dict[case]

        #조건의 유효기간이 100달까지 있기 때문에 그 기간동안 추가를 해줘야함. 
        while t_month > 12:
                t_year += 1
                t_month -= 12

        if t_year > year :
            continue        
        elif t_year == year :
            if t_month > month :
                continue                
            elif t_month == month :
                if t_day > day :
                    continue 
        answer.append(exam+1)
                
    return answer


print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))