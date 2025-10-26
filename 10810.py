# BOJ 10810: 공 넣기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):    # 1-indexed -> 0-indexed
        baskets[idx] = k

print(*baskets)
