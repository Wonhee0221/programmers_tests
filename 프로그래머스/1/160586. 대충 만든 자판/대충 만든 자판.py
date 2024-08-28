def solution(keymap, targets):
    # keymapㅇ을 돌면서 인덱스를 뽑아낸다.
    answer = []
    for i in targets:
        result = 0
        for x in i:
            flag = False
            min_list = 101
            for y in keymap:
                if x in y:
                    min_list = min(y.index(x)+1,min_list)
                    flag = True
            if not flag:
                result = -1
                break
            result += min_list
        answer.append(result)
    return answer