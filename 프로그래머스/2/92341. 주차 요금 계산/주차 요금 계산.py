import math
def solution(fees, records):
    numDict = dict()
    result = []
    basic_time = fees[0]
    basic_fee = fees[1]
    plus_time = fees[2]
    plus_fee = fees[3]
    final_price = 0
    for i in records:
        time = i[0:5].replace(":","")
        car_number = i[6:10]
        in_out = i[-3:].lstrip()
        if car_number in numDict:
            numDict[car_number].append([time,in_out])
        else:
            numDict[car_number] = [[time,in_out]]
    numDict = {key: numDict[key] for key in sorted(numDict.keys(), key=lambda x: int(x))}
    for x in numDict:
        resultTime = 0
        for y in range(len(numDict[x])):
            if numDict[x][y][1] == "IN":
                resultTime -= int(numDict[x][y][0][:2])*60+int(numDict[x][y][0][2:])
                if y + 1 == len(numDict[x]) or (y + 1 < len(numDict[x]) and numDict[x][y+1][1] != "OUT"):
                    resultTime += (23*60+59)  # 2359 추가
            elif numDict[x][y][1] == "OUT":
                
                resultTime += int(numDict[x][y][0][:2])*60+int(numDict[x][y][0][2:])
        print(resultTime)
        if resultTime <= basic_time:
            result.append(basic_fee)
        else:
            
            final_price= basic_fee + math.ceil(math.ceil((resultTime-basic_time)/plus_time)) * plus_fee
            result.append(final_price)

        
    return result