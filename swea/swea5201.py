T = int(input())
for test_case in range(1,T+1):
    cw,tw = map(int,input().split())
    cws = list(map(int,input().split()))
    tws = list(map(int,input().split()))
    cws.sort()
    tws.sort()
    answer = 0
    for i in range(cw):
        a = cws.pop()

        for j in tws:
            if a <= j:
                answer+=a
                tws.remove(j)
                break
    
    print(f'#{test_case} {answer}')