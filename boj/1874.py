import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(int(input()))]

answer = []
stack = []
num = 1  # 다음에 push할 숫자

for target in arr:
    
    # target까지 push
    while num <= target:
        stack.append(num)
        answer.append('+')
        num += 1
    
    # top이 target이면 pop
    if stack[-1] == target:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit()

print('\n'.join(answer))