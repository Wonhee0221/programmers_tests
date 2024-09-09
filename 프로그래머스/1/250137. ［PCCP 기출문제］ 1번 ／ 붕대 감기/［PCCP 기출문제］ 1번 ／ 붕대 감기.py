def solution(bandage, health, attacks):
    t, x, y = bandage
    go = 0  # 붕대 연속 성공 시간
    time = 0  # 현재 시간
    max_health = health  # 최대 체력
    now_health = health  # 현재 체력

    for attack in attacks:
        attack_time, attack_damage = attack
        
        # 공격이 발생하기 전까지 체력 회복
        while attack_time > time:
            if now_health <= 0:
                return -1

            go += 1  # 붕대 감기 성공 시간 카운트

            # 최대 체력일 경우에는 회복하지 않고 시간만 증가
            if now_health < max_health:
                now_health += x  # 1초당 회복량
                now_health = min(now_health, max_health)  # 최대 체력 초과 방지

            # 붕대 감기 성공 시 추가 회복
            if go == t:
                now_health += y
                now_health = min(now_health, max_health)  # 최대 체력 초과 방지
                go = 0  # 추가 회복 후 초기화

            time += 1  # 시간 경과
        
        # 공격을 받는 시간
        time += 1  # 공격 시간이 지나감
        now_health -= attack_damage  # 공격으로 체력 감소
        
        # 공격으로 체력이 0 이하가 되면 즉시 종료
        if now_health <= 0:
            return -1

        go = 0  # 공격 받으면 붕대 초기화
    
    return now_health
