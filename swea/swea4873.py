T  = int(input())
for test_num in range(1,T+1):
    L=[]
    L += input()
    stack = []
    for i in L:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_num} {len(stack)}')