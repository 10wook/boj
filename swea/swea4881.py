T = int(input())
from itertools import permutations
for test_num in range(1,T+1):
    answer = float('inf')
    N =int(input())
    L = [list(map(int,input().split())) for _ in range(N)]
    for picks in permutations(range(N),N):
        hap  = 0
        for i in range(N):
            hap+=L[i][picks[i]]
        answer = min(answer,hap)
    print(f'#{test_num} {answer}')