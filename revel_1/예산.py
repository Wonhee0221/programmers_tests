def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

#전체 부서별 신청금액보다 예산이 크면 가장 큰 금액을 지원한 부서부터 하나씩 값을빼서
#예산 내에서 모든 부서를 지원할 수 있을 때 부서의 수를 리턴한다.