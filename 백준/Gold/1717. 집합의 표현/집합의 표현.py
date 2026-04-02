import sys
input = sys.stdin.readline

def find(X):
    if X == L[X]:
        return X
    L[X] = find(L[X])
    return L[X]
def union(a, b):
    ra = find(a)  
    rb = find(b)  
    
    if ra != rb:
        L[rb] = ra 
        
        
N,M = map(int,input().split())
L = list(range(0,N+1))

for _ in range(M):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")