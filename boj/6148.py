from itertools import combinations

N, B = map(int, input().split())
cows = [int(input()) for _ in range(N)]

answer = float('inf')

for r in range(N + 1):
    for comb in combinations(cows, r):
        total = sum(comb)
        if total >= B:
            answer = min(answer, total)

print(answer - B)
