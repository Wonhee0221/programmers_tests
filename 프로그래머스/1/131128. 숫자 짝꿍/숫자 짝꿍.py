def solution(X, Y):
    answer = ''
    di_x = {str(i):0 for i in range(10)}
    di_y = {str(i):0 for i in range(10)}
    for i in X:
        di_x[i] +=1 
    for y in Y:
        di_y[y] +=1
    for x in range(9,-1,-1):
        x = str(x)
        qwe = min(di_x[x],di_y[x])
        if answer == '' and x == '0' and qwe != 0:
            return '0'
        answer = ''.join([answer,x*qwe])
    if answer == '':
        return "-1"
    return answer