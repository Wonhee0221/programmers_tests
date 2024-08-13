def solution(n):
    f = [0,1]
    for i in range(1,n+1):
        f.append(f[i]+f[i-1])
    return f[-1]%1234567