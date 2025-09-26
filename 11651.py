N = int(input())
L = []
for i in range(N):
    a,b = map(int,input().split())
    L.append([a,b])
    
L1 = sorted(L, key=lambda x : (x[1], x[0]))

for i in L1:
    print(i[0],i[1])