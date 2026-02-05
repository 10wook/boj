N = int(input())
L = input().split()
for i in range(N):
    L[i] = int(L[i])
    
M = max(L)
add = 0
for i in range(N):
    add += L[i]/M * 100
    
print(add/N)
