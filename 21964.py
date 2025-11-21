import sys

input = sys.stdin.readline

N = int(input().strip())
S = input().rstrip('\n')  # 개행만 제거

# 마지막 5글자 출력
print(S[-5:])