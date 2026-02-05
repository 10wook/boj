T = int(input())

for i in range(1,T+1):
    answer = -1
    M = 0
    N = int(input())
    S = input()
    for j in range(N):
        if S[j] == '1':
            M+=1
        if S[j] == '0':
            if answer < M:
                answer = M
            M = 0
            #이 부분 에러를 멍청하게 못 잡아서 문제가 이썽ㅆ음.
        if j == N-1:
            if answer < M:
                answer = M
    print(f'#{i} {answer}')




