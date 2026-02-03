T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    AL = []
    for j in range(N-M+1):
        
        AL.append(sum(L[j:j+M]))

    answer = max(AL) - min(AL)
    print(f'#{i} {answer}')