import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = sorted(A - B)

print(len(C))
if C:
    print(*C)