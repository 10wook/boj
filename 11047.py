N, K = map(int,input().split())
L =[]
for i in range(N):
    L.append(int(input()))
    
cnt = 0
for i in range(N-1,-1,-1):
    cnt += K//L[i]
    K = K%L[i]
            
print(cnt)