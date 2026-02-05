# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

# 1️⃣ 최대 n값 (조합의 n) 계산
max_n = max(b for _, b in L)

# 2️⃣ DP 테이블 초기화: C[n][k] = nCk
C = [[0]*(max_n+1) for _ in range(max_n+1)]

# 3️⃣ 점화식 적용
for n in range(max_n+1):
    for k in range(n+1):
        if k == 0 or k == n:
            C[n][k] = 1
        else:
            C[n][k] = C[n-1][k-1] + C[n-1][k]

# 4️⃣ 각 쿼리에 대해 출력
for a, b in L:
    print(C[b][a])
