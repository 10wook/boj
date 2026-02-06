T = int(input())
for test_num in range(1,T+1):
    A = input()
    B = input()
    l = []
    for i in range(len(A)):
        l.append(B.count(A[i]))
    print(f'#{test_num} {max(l)}')
