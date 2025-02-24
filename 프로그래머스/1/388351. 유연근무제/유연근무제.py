# 시간변환기
def transTime(time):
    h = time // 100
    minute = (time % 100) + 10
    if minute >= 60:
        minute -= 60
        h += 1
    return (h*100)+minute
def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        threshold = transTime(schedules[i])  # 허용 시간 (10분 추가)
        daily_logs = timelogs[i]       # 현재 스케줄의 타임로그
        current_day = startday         # 시작 요일부터 추적
        is_valid = True                # 조건 만족 여부
        for log in daily_logs:
            # 주말(토요일:6, 일요일:7)은 건너뜀
            if current_day in [6, 7]:
                current_day += 1
                if current_day == 8:   # 일요일 다음은 월요일
                    current_day = 1
                continue
            # 타임로그가 임계값을 초과하면 실패
            if log > threshold:
                is_valid = False
            # 다음 날짜로 이동
            current_day += 1
        # 조건을 만족하면 카운트 증가
        if is_valid:
            answer += 1
    
    return answer