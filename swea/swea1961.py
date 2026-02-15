T= int(input())
for test_num in range(1,T+1):
    N= int(input())
    origin = []
    for _ in range(N):
        origin.append(list(map(int,input().split())))
    list90 = [[0]*N for _ in range(N)]
    list180 = [[0]*N for _ in range(N)]
    list270 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            list90[j][N-1-i] = origin[i][j]
    for i in range(N):
        for j in range(N):
            list180[j][N-1-i] = list90[i][j]        
    for i in range(N):
        for j in range(N):
            list270[j][N-1-i] = list180[i][j]
    print(f'#{test_num}') 
    for i in range(N):
        print(*list90[i], ' ',*list180[i],' ' ,*list270[i], sep = '')