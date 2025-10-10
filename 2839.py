N = int(input())
import math
dp = [math.inf] * (N+1)
dp[0] = 0
for i in range(N+1):
    if i  < 5 :
        if i < 3:
            continue
        else:
            dp[i] = dp[i-3]+1
        
    else:
        dp[i] = min(dp[i-3]+1,dp[i-5]+1)
        
if dp[N] == math.inf:        
    print(-1)
else:
    print(dp[N])