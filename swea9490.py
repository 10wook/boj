T = int(input())
def range_check(x,y):
    global N,M
    if x < 0 or x >=N or y < 0 or y >=M:
        return False
    else:
        return True

def score(x,y,flwrpdr)->int:
    
    global N,M,board
    S = board[x][y]
    for i in range(1,flwrpdr+1):
        check = [(x+i,y),(x-i,y),(x,y+i),(x,y-i)]
        for j in check:
            if range_check(j[0],j[1]):
                S += board[j[0]][j[1]]
            else:
                pass
    return S

for test_num in range(1,T+1):
    N,M = map(int,input().split())
    board = []
    score_board = []
    for i in range(N):
        board.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(M):
            score_board.append(score(i,j,board[i][j]))
    print(f'#{test_num} {max(score_board)}')