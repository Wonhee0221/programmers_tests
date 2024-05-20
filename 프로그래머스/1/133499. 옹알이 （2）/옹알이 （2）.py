def solution(babbling):
    answer = 0
    for i in babbling:
        pre_word = ["aya", "ye", "woo", "ma"]
        word = ""
        word_x = ""
        for j in i:
            word+=j
            if word in pre_word:
                orgin_word  = word
                if word_x != word:
                    word = word.replace(word,"")
                word_x = orgin_word
        if len(word) <1:
            answer +=1
        else:
            print(word)
    return answer