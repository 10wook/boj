import sys
from functools import lru_cache
sys.setrecursionlimit(200000)

N,K = map(int,input().split())
items = []
for i in range(N):
    items.append(list(map(int, input().split())))

#앞에 입력이 무게임
DP_list = []
for i in range(N):
    DP_list.append([])
    for j in range(K+1):
        DP_list[i].append(-1)
@lru_cache(None)        
def DP(N,K):
    if N < 0 or K == 0:
            return 0
    if DP_list[N][K] != -1:
            return DP_list[N][K] 
        
    if K < items[N][0]:
            # 현재 물건을 못 넣음
        value = DP(N-1, K)
    else:
        value = max(DP(N-1,K),(DP(N-1,K-items[N][0])+items[N][1]))
        DP_list[N][K] = value

    

    return value

print(DP(N-1,K))