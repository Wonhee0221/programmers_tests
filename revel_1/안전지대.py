import copy
def solution(board):
    cnt = 0
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for x in range(3):
                    if new_board[i][j-x] == "":
                        continue
                    else:
                        new_board[i-x][j-x] = 1
                    if new_board[i-x][j+x] == "":
                        continue
                    else:
                        new_board[i-x][j+x] = 1
                    if new_board[i-x][j] == "":
                        continue
                    else:
                        new_board[i-x][j] = 1
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 0:
                cnt += 1
    return cnt

print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))





                    
                    