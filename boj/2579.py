N = int(input())
L = [int(input()) for _ in range(N)]

# 메모이제이션 리스트
dp = [-1] * N

def cal(index):
    # base case
    if index == 0:
        return L[0]
    if index == 1:
        return L[0] + L[1]
    if index == 2:
        return max(L[0] + L[2], L[1] + L[2])
    
    if dp[index] != -1:  # 이미 계산된 경우
        return dp[index]
    
    # 점화식 적용
    dp[index] = max(
        cal(index-2) + L[index],         # i-2에서 점프
        cal(index-3) + L[index-1] + L[index]  # i-3 -> i-1 -> i
    )
    return dp[index]

print(cal(N-1))
