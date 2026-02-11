T = int(input())

for test_num in range(1,T+1):
    num_stack = []
    # func_stack = []
    answer  = 'error'
    for s in input().split():
        if s.isdigit():
            num_stack.append(int(s))
        elif s == '.':
            if len(num_stack) == 1:
                answer = num_stack[0]
            else:
                answer = 'error'
            break
        else:
            if len(num_stack) < 2:
                answer = 'error'
                break
            b = num_stack.pop()
            a = num_stack.pop()
            if s =='*':
                    num_stack.append(a*b)
            if s =='/':
                if b == 0:
                    answer = 'error'
                    break

                num_stack.append(a//b)
            if s =='+':
                    num_stack.append(a+b)
            if s =='-':
                    num_stack.append(a-b)
    print(f'#{test_num} {answer}')