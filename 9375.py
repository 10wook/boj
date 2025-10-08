N = int(input())
L = []
for i in range(N):
    M = int(input())
    d = {}
    for j in range(M):

        a,b = input().split()
        if b in d:
            d[b] +=1
        else:
            d[b] = 1
    cnt = 1
    for k in d:
            cnt *= (d[k]+1)
    L.append(cnt-1)
for i in L:
    print(i)