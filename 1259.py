while True:
    A = input()
    if A =='0':
        break
    A = list(A)
    B = []
    for i in range(len(A)-1,-1,-1):
        B.append(A[i])
    if A == B:
        print('yes')
    else:
        print('no')