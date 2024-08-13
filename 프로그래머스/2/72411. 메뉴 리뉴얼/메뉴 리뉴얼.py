from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for course_size in course:
        course_menus = []
        
            # 각 주문에서 course_size에 해당하는 조합 구하기
        for order in orders:
            course_menus += combinations(sorted(order), course_size)
        

            # 각 조합의 주문 횟수 세기
        course_counter = Counter(course_menus)
        print(course_counter)

            # 가장 많이 주문된 조합 중 최소 2명 이상의 손님에 의해 주문된 것만 선택
        max_count = 0
        for menu, count in course_counter.items():
            if count > 1 and count >= max_count:
                max_count = count

            # 주문 횟수가 최대인 메뉴들 추가
        for menu, count in course_counter.items():
            if count == max_count:
                answer.append("".join(menu))
    
    # 사전 순으로 정렬
    answer.sort()
    return answer