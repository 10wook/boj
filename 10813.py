N,M = map(int,input().split())
L  = list(range(N))
for i in range(M):
    n,m = map(int,input().split())
    L[n-1],L[m-1] = L[m-1],L[n-1]
    
for i in range(N):
    print(L[i]+1,end=' ')