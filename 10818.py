N = int(input())
L = input().split()
for i in range(N):
    L[i] = int(L[i])
print(str(min(L))+' '+str(max(L)))