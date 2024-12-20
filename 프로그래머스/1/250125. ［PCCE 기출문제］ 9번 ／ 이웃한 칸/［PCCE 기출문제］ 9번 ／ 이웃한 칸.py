def solution(board, h, w):
    color = board[h][w] 
    answer = 0
    N = len(board)
    dx, dy = [0,0,-1,1], [1,-1,0,0]
    for i in range(4):
        nx = w + dx[i]
        ny = h + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if board[ny][nx] == color:
                answer += 1
    return answer