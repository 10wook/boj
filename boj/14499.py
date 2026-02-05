N, M, r,c, moves = map(int, input().split())
L = []
for i in range(N):
    L.append(input().split())
    
for i in range(N):
    for j in range(M):
        L[i][j] = int(L[i][j])

        
ML = list(map(int, input().split()))

#1. 주사위 상태 확인하기 - 기능 필요
'''
  2  
4 1 3
  5
  6
'''
# 이거를 순서대로 맨위 왼 쪽 부터 읽은거임
# 인덱스 위치로 계산을 하면 되지 않을까??
'''[맨 위,앞 방향,오른 쪽 방향, 왼쪽 방향, 뒤쪽 방향, 맨 아래]'''
dice_state = [0,0,0,0,0,0]


# 2. 주사위를 굴리는 기능 필요
def roll_dice(dice:list,dir:int):
    new_dice = [0,0,0,0,0,0]
    if dir ==1:#동 쪽으로 
        ## 3번째 자리가 6번 바닥으로,1이 3번 자리로, 4번이 1번 자리로, 6번 자리가 4번 자리로
        new_dice[5] = dice[2]
        new_dice[2] = dice[0]
        new_dice[0] = dice[3]
        new_dice[3] = dice[5] 
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    if  dir ==2:
        new_dice[2] = dice[5]
        new_dice[0] = dice[2]
        new_dice[3] = dice[0]
        new_dice[5] = dice[3] 
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    if dir == 3:
        new_dice[1] = dice[0]
        new_dice[0] = dice[4]
        new_dice[4] = dice[5]
        new_dice[5] = dice[1] 
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
    if dir == 4:
        new_dice[0] = dice[1]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
        new_dice[1] = dice[5] 
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]        
    return new_dice

# 주사위의 상태를 변경하는 기능 - 주사위가 이동 후 어떤 식으로 놓여 있을 것인지
# 보드 위에서 어느 위치에 주사위가 놓여 있을 것 인지 상태 변경
def dice_num_change(dice:list, board:list, dice_loc:list):
    if board[dice_loc[0]][dice_loc[1]] == 0 :
        board[dice_loc[0]][dice_loc[1]]  = dice[5]

    else :
        dice[5] = board[dice_loc[0]][dice_loc[1]]
        board[dice_loc[0]][dice_loc[1]] = 0
    pass


# 3. 주사위 굴린 이후 보드의 숫자와 주사위의 숫자가 바뀌는 기능 필요

def move_dice(board:list,dir :int,dice_loc:list  ):
    new_dice_loc = [0,0]
    if dir == 1:
        if dice_loc[1]+1 >= M:
            return dice_loc,False
        else:
            new_dice_loc[0] = dice_loc[0]
            new_dice_loc[1] = dice_loc[1]+1
    elif dir == 2:
            if dice_loc[1]-1 < 0:
                return dice_loc,False
            else:
                new_dice_loc[0] = dice_loc[0]
                new_dice_loc[1] = dice_loc[1]-1        
    elif dir == 4:
        if dice_loc[0]+1 >= N:
                return dice_loc,False
        else:
                new_dice_loc[0] = dice_loc[0]+1
                new_dice_loc[1] = dice_loc[1]
    elif dir == 3:
            if dice_loc[0]-1 < 0:
                return dice_loc,False
            else:
                new_dice_loc[0] = dice_loc[0]-1
                new_dice_loc[1] = dice_loc[1]  
    return new_dice_loc,True



# 4.  주사위를 움직일때 제한을 거는 기능 필요.



def dice_print(dice:list):
    print(dice[0])




# 5.  주사위 맨 위에 있는 숫자 출력하는 기능 필요


# 하나씩 구현하고, 함수로 하나씩 조합해서 돌리면 될듯.

dice_loc = [r,c]

for i in ML:
    dice_loc, m = move_dice(L,i,dice_loc)
    if m == True:
        dice_state = roll_dice(dice_state,i)
        dice_num_change(dice_state,L,dice_loc)
        dice_print(dice_state)