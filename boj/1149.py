N = int(input())
RGBs = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]
choice = [[-1]*3 for _ in range(N)]

dp[0] = RGBs[0][:]

for i in range(1, N):
    for c in range(3):
        # (비용, 색 인덱스) 튜플로 비교
        prev = [(dp[i-1][x], x) for x in range(3) if x != c]
        min_val, min_color = min(prev)
        dp[i][c] = RGBs[i][c] + min_val
        choice[i][c] = min_color

# 최소비용 결과
last_color = min(range(3), key=lambda x: dp[N-1][x])
min_cost = dp[N-1][last_color]


print( min_cost)

