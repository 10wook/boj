N = int(input())
L = input().split()
for i in range(N):
    L[i] = int(L[i])
    
L.sort()
# print(L)

cnt = 0
a= 0
for i in L:
    cnt +=i
    a +=cnt
    # print(cnt)
    
    
print(a)