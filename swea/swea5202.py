T = int(input())
for test_num in range(1,T+1):
    N = int(input())
    L = [tuple(map(int,input().split())) for _ in range(N)]

    L.sort(key=lambda x:(x[1],x[0]))

    curr = 0
    cnt = 0

    for s,e in L:
        if s >= curr:
            curr = e
            cnt +=1

    print(f'#{test_num} {cnt}')