def solution(s, n):
    x = ''
    for i in s:
        if i == " ":
            x += " "
        elif ord('a') <= ord(i) <=ord('z') :
            if ord(i) + n > ord('z'):
                x+=chr(ord(i)+n-26)
            else:
                x+=chr(ord(i)+n)
        else:
            if ord(i) + n > ord('Z'):
                x+=chr(ord(i)+n-26)
            else:
                x+=chr(ord(i)+n)
    
    return x