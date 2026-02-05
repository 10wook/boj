L = []
for i in range(9):
    L.append(list(map(int,input().split())))
    
M = -1
I = -1
J = -1
for i in range(9):
    for j in range(9):
        if L[i][j] > M:
            M = L[i][j]
            I = i
            J = j
            
            
print(M)
print(I+1,J+1)