N = int(input())
from itertools import combinations_with_replacement
board = []

board = [list(map(int,input().split())) for _ in range(N)]
# print(board)
stack = []
#앞으로 어디로 움직일지 정하는 스택
board_stats = []
board_stats.append(board)

def merge(line):
    new = [x for x in line if x != 0]
    merged = []
    i = 0
    while i < len(new):
        if i+1 < len(new) and new[i] == new[i+1]:
            merged.append(new[i]*2)
            i += 2
        else:
            merged.append(new[i])
            i += 1
    merged += [0]*(N-len(merged))
    return merged
#여기다가 보드 상태를 담는 방식으로 이용하면 될거 같고, 그리고 
def move(board, cmd):
    new_board = [[0]*N for _ in range(N)]

    # 왼쪽
    if cmd == 1:
        for i in range(N):
            new_board[i] = merge(board[i])

    # 오른쪽
    elif cmd == 0:
        for i in range(N):
            new_board[i] = merge(board[i][::-1])[::-1]

    # 위
    elif cmd == 3:
        for j in range(N):
            col = [board[i][j] for i in range(N)]
            merged = merge(col)
            for i in range(N):
                new_board[i][j] = merged[i]

    # 아래
    elif cmd == 2:
        for j in range(N):
            col = [board[i][j] for i in range(N)][::-1]
            merged = merge(col)[::-1]
            for i in range(N):
                new_board[i][j] = merged[i]

    return new_board


def DFS(depth, board):
    if depth == 6:
        return max(map(max, board))

    return max(
        DFS(depth+1, move(board,0)),
        DFS(depth+1, move(board,1)),
        DFS(depth+1, move(board,2)),
        DFS(depth+1, move(board,3))
    )

print(DFS(1, board))