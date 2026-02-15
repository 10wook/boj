T= int(input())
for test_num in range(1,T+1):
    N= int(input())
    origin = []
    for _ in range(N):
        origin.append(list(map(int,input().split())))
    list90 = [[0]*N for _ in range(N)]
    print(f'#{test_num}') 
    print(list90)