from collections import deque
def solution(bridge_length, weight, truck_weights):
    roof = len(truck_weights)
    truck_que = deque(truck_weights)
    answer = 0
    que = deque([0] * bridge_length)
    if roof == 1:
        return bridge_length + roof
    now = 0
    while truck_que:
        answer += 1
        now -= que.popleft()
        if now + truck_que[0] <= weight:
            now += truck_que[0]
            que.append(truck_que.popleft())
        else:
            que.append(0)
    answer += bridge_length
    return answer