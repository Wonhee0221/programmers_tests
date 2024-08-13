import re
def solution(dartResult):
    answer = []
    bonus = {"S":1,"D":2,"T":3}
    parts = re.findall(r'\d+[^\d]*', dartResult)
    for part in parts:
        other = len(part)
        letters = re.split(r'([a-zA-Z])', part)
        if other == 2:
            x = int(letters[0]) ** bonus[letters[1]]
            answer.append(x)
        else:
            x = int(letters[0]) ** bonus[letters[1]]
            if letters[2] == "#":
                x *= (-1)
                answer.append(x)
            elif letters[2] == "*":
                if len(answer) > 0:
                    x *= 2
                    answer[-1] = answer[-1]*2
                    answer.append(x)
                else:
                    x *= 2
                    answer.append(x)
            else:
                answer.append(x)
    return sum(answer)