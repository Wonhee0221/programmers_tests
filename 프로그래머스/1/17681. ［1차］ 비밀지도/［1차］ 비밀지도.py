def solution(n, arr1, arr2):
    arrys = []
    arrys2 = []
    answer = []
    ansstr =""
    for i in range(n):
        two = format(arr1[i],'b')
        if len(two) < n:
            two = (n- len(two)) * '0'+two 
        arrys.append(two)
    for i in range(n):
        two = format(arr2[i],'b')
        if len(two) < n:
            two = (n- len(two)) * '0'+two 
        arrys2.append(two)
        
    for x in range(n):
        ansstr =""
        for i in range(n):
            if arrys[x][i] == "1" or arrys2[x][i] == "1":
                ansstr +="#"
            else:
                ansstr += " "
        answer.append(ansstr)

    return answer