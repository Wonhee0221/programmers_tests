def solution(lottos, win_nums):
    max_lotto=0
    min_lotto=0
    for i in win_nums:
        if i in lottos:
            max_lotto += 1
            min_lotto += 1
    max_lotto += lottos.count(0)
    lotto_dict = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    answer = [lotto_dict[max_lotto],lotto_dict[min_lotto]]
    return answer