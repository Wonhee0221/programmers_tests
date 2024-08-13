def solution(N, stages):
    dict_N = {i:0 for i in range(1,N+1)}
    stage_peple = len(stages)
    for i in range(1,N+1):
        fail = stages.count(i)
        if fail:
            dict_N[i] = fail/stage_peple
            stage_peple -= fail
    answer = sorted(dict_N.keys(), key=lambda x: (-dict_N[x], x))
    return answer