T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    status = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        hap = [0]
        for x in temp:
            hap.append(hap[-1] + x)
        status.append(hap)
    #파리상태 입력까지는 받았음 (가로행 누적합으로 받았음)
    snap = []
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            snap_once = 0
            for dr in range(M):
                snap_once += status[r + dr][c + M] - status[r + dr][c]
            snap.append(snap_once)
        
    print(f'#{test_num} {int(max(snap))}')
    

