N ,M = map(int, input().split())
oN,oM = N,M
N_L = [0]
for i in range(1,N+1):
    cnt = 0
    while True:
        if N%(i+1) != 0:
            break
        else:
            N = N/(i+1)
            cnt += 1
    N_L.append(cnt)
M_L = [0]    
for i in range(1,M+1):
    cnt = 0
    while True:
        if M%(i+1) != 0:
            break
        else:
            M = M/(i+1)
            cnt += 1
    M_L.append(cnt)
small = 1
for i in range (min(oN,oM)):
    if min(N_L[i],M_L[i]) == 0:
        pass 
    else:
        ##그 범위의 횟수 만큼 곱해야 할거 아니냐
        for j in range(min(N_L[i],M_L[i])):
            small = small * (i+1)
        
        
big = 1
a = max(oN,oM)
for i in range (a):
    if i >= len(N_L):
        big *= (i+1) **  M_L[i]
        continue
    if i >= len(M_L):
        big *= (i+1) **  N_L[i]
        continue
    if N_L[i] or M_L[i]:
            big *= (i+1) ** max(N_L[i], M_L[i])
    



print (small)
print(big)