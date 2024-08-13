def solution(s, skip, index):
    answer = ''
    skip_word = [ord(i) for i in skip]
    for word in s:
        word_loc = ord(word)
        cnt = index
        while cnt != 0:
            word_loc+=1
            if  word_loc > ord('z'):
                word_loc = word_loc - ord('z') + ord('a')-1
            if word_loc in skip_word:
                continue
            cnt-=1
        answer +=chr(word_loc)    
    return answer 