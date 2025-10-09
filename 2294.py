import sys,math
from functools import lru_cache
sys.setrecursionlimit(900000000)
input = sys.stdin.readline
N,K = map(int,input().split())
coins =set()
for i in range(N):
    coins.add(int(input()))


#15를 만드는데 동전 몇개를 사용해서 만들거냐.
#최대한 적게 만들기
#
dp = [math.inf] * (K + 1)
dp[0] = 0

for i in range(1, K + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[K] if dp[K] != math.inf else -1)
