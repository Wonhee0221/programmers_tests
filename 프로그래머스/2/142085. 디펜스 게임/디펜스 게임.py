import heapq
def solution(n, k, enemy):
    answer = 0
    storage= []
    # 먼저 k(무적권) 이 상대해야하는 라운드보다 같거나 많을때는 무조건 쓰면됌
    if k >= len(enemy):
        return len(enemy)
    # k 개까지는 그냥 넣는다. 그다음에는 넣고 맨 마지막수를 빼고 n 에다가 뺀다. n이 최소보다 작을 때까지하고 k를 더한다.
    total_damage = 0  # 무적권 없이 막아야 하는 데미지 합
    for x in enemy:
        heapq.heappush(storage, x)  # 최대 힙 효과를 위해 음수로 삽입
        # storage 크기가 k를 초과하면 가장 작은 값(음수로 인해 실제로는 가장 큰 데미지)을 뺌
        if len(storage) > k:
            total_damage += heapq.heappop(storage)  # 음수를 다시 양수로 변환해 더함
            # n보다 total_damage가 크면 더 이상 진행 불가
            if total_damage <= n:
                answer += 1
            else:
                break
    return answer + k