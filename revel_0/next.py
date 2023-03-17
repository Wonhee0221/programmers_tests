def solution(my_string, letter):
    my_string.remove(letter)
    return my_string
print(solution("abcdef", "f"))