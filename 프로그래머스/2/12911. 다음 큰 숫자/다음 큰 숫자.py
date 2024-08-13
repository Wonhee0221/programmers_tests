def solution(n):
    two = bin(n).count("1")
    while True:
        n+=1
        if two == bin(n).count("1"):
            break   
    return n