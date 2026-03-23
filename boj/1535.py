N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0] * 100  # 체력 0~99

for i in range(N):
    for h in range(99, L[i]-1, -1):
        dp[h] = max(dp[h], dp[h - L[i]] + J[i])

print(dp[99])