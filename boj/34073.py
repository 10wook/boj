import sys

input = sys.stdin.readline
N = int(input().strip())
words = input().strip().split()

print(' '.join(w + 'DORO' for w in words))
