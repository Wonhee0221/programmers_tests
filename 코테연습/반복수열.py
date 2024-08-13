a, p = map(int,input().split())
answer = []

def bfs(a):
    answer.append(a)   
    while answer:
        total_result = 0
        for digit in str(answer[-1]):
            total_result += int(digit) ** p        
        if total_result in answer:
            break
        answer.append(total_result)    
    return answer.index(total_result) # 반복이 시작되는 값전까지의 인덱스를 구하면 갯수를 구할 수 있다.
print(bfs(a))
