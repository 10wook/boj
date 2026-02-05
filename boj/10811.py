import sys

input = sys.stdin.readline

N, M = map(int, input().split())
baskets = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    # i~j 구간을 역순으로
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)
