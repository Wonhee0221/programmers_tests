def solution(skill, skill_trees):
    answer = 0
    for x in skill_trees:
        success = True
        nskill = skill
        for t in x:
            ## 돌면서 만약에 t 가 스킬트리에 있으면서 가장 먼저꺼라면 ㅇㅋ하고 앞에거 지우고 계속
            if t in skill:
                if nskill[0] == t:
                    nskill = nskill[1:]
                else:
                    success = False
                    break
            else:
                continue
        if success:
            answer+=1
    return answer