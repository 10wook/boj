A = int(input())

for i in range(A):
    K = int(input()) # 1
    N = int(input()) # 3
    L = []
    L.append(list(range(1,N+1)))
    # print(L)
    for i in range(K): #==>층수
        L.append([]) 
        for j in range(N): #==> 호수
            L[-1].append(sum(L[-2][:j+1]))

    print(L[-1][-1])
