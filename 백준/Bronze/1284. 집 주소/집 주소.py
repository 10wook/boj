import sys
input = sys.stdin.readline

width = {'1': 2, '0': 4}

while True:
    N = input().strip()
    if N == '0':
        break
    total = 2  # 양쪽 경계 1cm씩
    total += len(N) - 1  # 숫자 사이 여백
    for c in N:
        total += width.get(c, 3)
    print(total)