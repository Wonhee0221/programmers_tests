def solution(msg):
    answer = []
    alphas = {}
    for x in range(1,26+1):
        alphas[chr(64+x)] = x
    word = 0
    c = 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(alphas[msg[word:c]])
            break
        if msg[word:c+1] not in alphas:
            alphas[msg[word:c+1]] = len(alphas)+1
            answer.append(alphas[msg[word:c]])
            word = c
    return answer