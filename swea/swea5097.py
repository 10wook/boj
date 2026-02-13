T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    print(f'#{test_num} {L[M%N]}')