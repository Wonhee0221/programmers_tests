def solution(diffs, times, limit):
    min_diffs, max_diffs = 1, max(diffs)
    answer = 0
    def isOK (mid):
        count = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                count += times[i]
            else:
                dis = diffs[i] - mid # 2
                count += (times[i] + times[i-1]) * dis + times[i]
            if count > limit:
                return False
        if count <= limit:
            return True
        else:
            return False
    while min_diffs <= max_diffs:
        mid = (max_diffs + min_diffs)//2
        if isOK(mid):
            answer = mid
            max_diffs = mid - 1
        else:
            min_diffs = mid + 1
    return answer