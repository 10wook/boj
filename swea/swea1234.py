
for test_num in range(1,10+1):
    A,B = input().split()
    L=[]

    L += B
    stack = []
    for i in L:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{test_num} ',*stack,sep='')