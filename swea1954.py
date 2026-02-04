
def move(x,y,dir):
    if dir == 0:
        return x,y+1
    elif dir == 1:
         return x+1,y
    elif dir == 2:
        return x,y-1
    else :
         return x-1,y
def turn_check(x,y):
    global answer
    global N
    if x < 0 or y < 0 or x==N or y==N:
        return True
    elif answer[x][y] !=0:
        return True
    else:
        return False
def  turn(dir:int ):
    if dir ==3:
        return 0
    else:
        return dir +1
    
T = int(input())
for testcase in range(1,T+1):
    direction = 0 #오른쪽 0 /아래 1/ 왼쪽 2/위쪽 3
    N = int(input())
    answer = [[0]*N for _ in range(N)]
    x,y = 0,0
    for steps in range(1, N*N+1):
        #벽이나 채워진 칸을 만나면 오른쪽으로 방향을 튼다.
        # 이 칸에 스텝 번호로 넣는다.
        answer[x][y] = steps
        # print(answer)
        dest_x,dest_y = move(x,y,direction)
        if turn_check(dest_x,dest_y):
            direction=turn(direction)
            dest_x,dest_y = move(x,y,direction)
        else:
            pass
        x,y = dest_x,dest_y
    print(f'#{testcase}')
    for i in answer:
        print(* i)