import sys

input = sys.stdin.readline
N = int(input())
# print(N)
stack = []
for i in range(N):
    func = input().strip()
    # print(func)
    if ' ' in func:
        func, num = func.split()
    # print(func)

    if func == 'push':
        stack.append(num)
        pass
    elif func == 'top':
        # print('length',len(stack))
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
        pass 
    elif func == 'size':
        # print('length',len(stack))
        print(len(stack))
        pass 
    elif func == 'empty':
        # print('length',len(stack))
        if len(stack) ==0:
            print(1)
        else:
            print(0)
        pass 
    elif func == 'pop':
        # print('length',len(stack))
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        pass 
    # print(stack)