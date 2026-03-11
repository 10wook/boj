T = int(input())

for test_num in range(1, T+1):
    P, A, B = map(int, input().split())

    Acnt = 0
    Bcnt = 0

    start, end = 1, P
    while True:
        Acnt += 1
        mid = (start + end) // 2
        if mid == A:
            break
        elif mid < A:
            start = mid
        else:
            end = mid

    start, end = 1, P
    while True:
        Bcnt += 1
        mid = (start + end) // 2
        if mid == B:
            break
        elif mid < B:
            start = mid
        else:
            end = mid

    if Acnt < Bcnt:
        print(f'#{test_num} A')
    elif Acnt > Bcnt:
        print(f'#{test_num} B')
    else:
        print(f'#{test_num} 0')