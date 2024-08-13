from collections import deque

def bfs(begin, target, words):
    que = deque([(begin, 0)])
    visited = set(begin)
    
    while que:
        x, step = que.popleft()
        if x == target:
            return step
        
        for word in words:
            if sum(a != b for a, b in zip(x, word)) == 1 and word not in visited:
                visited.add(word)
                que.append((word, step + 1))
    
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0  
    return bfs(begin, target, words)
