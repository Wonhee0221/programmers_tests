def solution(data, ext, val_ext, sort_by):
    answer = []
    dict_data = {"code":0, "date":1, "maximum":2, "remain":3}
    q1 = dict_data[ext]
    q2 = dict_data[sort_by]
    for x in data:
        if x[q1] <= val_ext:
             answer.append(x)
    answer = sorted(answer, key = lambda x:x[q2])
    return answer