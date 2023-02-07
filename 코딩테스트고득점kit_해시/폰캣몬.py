#코딩테스트 고득점 kit/해시/revel1(폰캣몬)
def solution(nums):
    answer = len(nums)//2
    t = set(nums)
    if len(t) >= answer:
        return answer
    else:
        return len(t)
    
#other
def solution(ls):
    return min(len(ls)/2, len(set(ls)))