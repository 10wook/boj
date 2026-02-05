import sys

input = sys.stdin.readline

N = int(input().strip())

student = [input().strip() for _ in range(N)]
answer  = [input().strip() for _ in range(N)]

correct = 0
for i in range(N):
    if student[i] == answer[i]:
        correct += 1

print(correct)