T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    # 잘라서 일단 넣어보고...
    #세트로 저장하면 될 듯
    S =set()
    cnt = 0
    for i in range(0,2*M,2):
        if (L[i],L[i+1]) in S or (L[i+1],L[i]) in S:
            cnt +=1
        S.add((L[i],L[i+1]))
        S.add((L[i+1],L[i]))
    # print(S)
    if N>M:
        print(f'#{test_num} {N-len(S)//2+cnt}')
    else:
        print(f'#{test_num} {1}')