T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    bombs = []
    for _ in range(N):
        bombs.append(list(map(int,input().split())))
    answer = 0
    for i in range(N):
        for j in range(M):
            temp = bombs[i][j]
            for blast in range(1,bombs[i][j]+1):
                for delta in range(4):
                    if 0<=i+dx[delta]*blast<N and 0<=j+dy[delta]*blast<M:
                        temp+= bombs[i+dx[delta]*blast][j+dy[delta]*blast]
            if temp > answer:
                answer =temp
    print(f'#{test_num} {answer}')