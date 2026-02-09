board = []
for _ in range(5):
    board.append(list(map(int,input().split())))
calls = []
for _ in range(5):
    calls.append(list(map(int,input().split())))
def bingo_check(board):
    target = (-1, -1, -1, -1, -1)
    cnt = 0
    for col in zip(*board):
        if col == target:
            cnt+=1
# 세로 검사
    for row in board:
        if tuple(row) == target:
            cnt+=1

    # 대각선 검사
    if tuple(board[i][i] for i in range(5)) == target:
        cnt+=1

    if tuple(board[i][4-i] for i in range(5)) == target:
        cnt+=1
        
    return cnt
end = False
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if calls[i][j] == board[k][l]:
                    board[k][l] = -1
                    if bingo_check(board) >=3:
                        print(j+(5*i)+1)
                        end = True
                        break

            if end == True:
                break
        if end == True:
            break
    if end == True:
        break