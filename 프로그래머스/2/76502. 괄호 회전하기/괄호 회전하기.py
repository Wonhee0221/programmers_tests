def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack

def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_valid(s):
            answer += 1
        s = s[1:] + s[:1]

    return answer