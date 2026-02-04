T = int(input())
for testcase in range(1,T+1):
    arr = [[0]*10 for _ in range(10)]
    answer = 0
    squares = int(input())
    for _ in range(squares):
        x1,y1,x2,y2,color = map(int,input().split())
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] +=color
                if arr[x][y] == 3:
                    answer +=1
    print(f'#{testcase} {answer}')