def solution(players, m, k):
    answer = 0
    pred_server = []
    for x in players:
        if len(pred_server) == 0 and x >= m:
            server = (x//m) - len(pred_server)
            answer += server
            for c in range(server):
                pred_server.append(0)
        elif len(pred_server) != 0 and (len(pred_server) * m) + m-1 < x:
            server = (x//m) - len(pred_server)
            answer += server
            for c in range(server):
                pred_server.append(0)
        pred_server = [x+1 for x in pred_server if x+1 !=k]
    return answer