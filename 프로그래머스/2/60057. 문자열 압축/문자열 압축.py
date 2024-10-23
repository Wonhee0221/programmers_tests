from collections import Counter
def solution(s):
    answer = 10000
    # s 의 길이가 1 일 경우 바로 리턴
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
        str_list  = ''
        tmp = s[:i]
        # 1개의 단위 부터 시작
        cnt = 1
        for j in range (i,len(s),i):
            if tmp == s[j:j+i]:
                cnt +=1
            else:
                if cnt > 1:
                    str_list += str(cnt) + tmp
                else:
                    str_list += tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt > 1:
            str_list += str(cnt) + tmp
        else:
            str_list += tmp
        if answer > len(str_list):
            answer = len(str_list)

        
    return answer