T = int(input())
from itertools import combinations
for test_num in range(1,T+1):
    cnt = 0
    N,K = map(int,input().split())
    for combi in combinations(range(1,13),N):
        if sum(combi) == K:
            cnt+=1
    print(f'#{test_num} {cnt}')