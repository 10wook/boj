import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

def value_fraction(a, b, c, d):
    # a/c + b/d = (a*d + b*c) / (c*d)
    return a*d + b*c, c*d  # (numerator, denominator)

best_k = 0
best_num, best_den = value_fraction(A, B, C, D)

# 현재 (A,B; C,D)를 시계방향으로 한 번 돌리면 (C,A; D,B)
a, b, c, d = A, B, C, D
for k in range(1, 4):
    a, b, c, d = c, a, d, b  # rotate 90° clockwise
    num, den = value_fraction(a, b, c, d)
    # 비교: num/den ? best_num/best_den
    if num * best_den > best_num * den:  # 더 크면 갱신 (같으면 그대로 두어 작은 k 유지)
        best_k = k
        best_num, best_den = num, den

print(best_k)
