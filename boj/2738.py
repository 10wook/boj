N,M = map(int,input().split())
L1 =[]
L2 =[]
for i in range(N):
    L1.append(list(map(int,input().split())))
for i in range(N):
    L2.append(list(map(int,input().split())))
    

for i in range(N):
    
    for j in range(M):
        print(L1[i][j]+L2[i][j],end=' ')
    print('')   
