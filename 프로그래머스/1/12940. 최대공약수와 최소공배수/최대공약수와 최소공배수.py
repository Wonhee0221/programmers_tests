def solution(n, m):
    def recursion(mi, ma):     
        r = ma % mi
        if r == 0:
            return mi 
        return recursion(r, mi)

    g = recursion(n, m)
    
    return [g, (n*m) // g]