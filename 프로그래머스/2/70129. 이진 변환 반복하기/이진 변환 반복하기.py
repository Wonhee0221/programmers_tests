def solution(s):
    answer = []
    cnt = 0 
    zeroCnt = 0
    word = s
    while True:
        cnt+=1
        zeroCnt += s.count('0')
        s = s.replace('0','')
        s = format(len(s),'b')
        if s == "1":
            break
        
    return [cnt,zeroCnt]