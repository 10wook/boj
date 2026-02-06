T = int(input())
for test_num in range(1,T+1):
    A = input()
    B = input()
    if A in B:
        print(f'#{test_num} {1}')
    else:
        print(f'#{test_num} {0}')