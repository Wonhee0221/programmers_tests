def solution(s):
    c = []
    for i in s:
        if i == '(':
            c.append(1)
        elif c:
            c.pop()
        else:
            return False
    if c:
        return False
    return True