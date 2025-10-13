import sys

for line in sys.stdin:
    A, B, C = map(float, line.split())
    cnt = 0
    while A <= C:
        A *= (1 + B / 100)
        cnt += 1
    print(cnt)
