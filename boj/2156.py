N = int(input())
L = [int(input()) for _ in range(N)]

if N == 1:
    print(L[0])
else:
    dp = [0]*N
    dp[0] = L[0]
    dp[1] = L[0] + L[1]  # 첫 두 잔까지의 최댓값

    for i in range(2, N):
        take_i_only = dp[i-2] + L[i]                             # i만 마심( i-1은 건너뜀 )
        take_i_and_prev = (dp[i-3] if i >= 3 else 0) + L[i-1] + L[i]  # i-1, i 연속으로 마심
        dp[i] = max(dp[i-1], take_i_only, take_i_and_prev)       # i는 안 마심 / i만 / i-1,i

    print(dp[-1])  # 정답
