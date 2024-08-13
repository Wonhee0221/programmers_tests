def solution(cacheSize, cities):
    city = []
    answer = 0
    if cacheSize <1:
        return len(cities)*5
    for i in cities:
        i=i.upper()
        if i in city:
            answer += 1
            city.remove(i)
            city.append(i)
        else:
            city.append(i)
            answer += 5
        if len(city) > cacheSize:
            city.remove(city[0])
            
    
    return answer


