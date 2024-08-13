def solution(n,a,b):
    answer = 0
    a,b= min(a,b),max(a,b)
    for i in range(1,n+1):
        a = a//2 + a%2
        b = b//2 + b%2
        answer +=1
        if a == b:
            break;
    return answer