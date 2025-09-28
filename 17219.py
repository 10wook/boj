N,M = map(int,input().split())  
memo = dict()
for i in range(N):
    a,b = input().split()
    memo[a]=b
L = []
for i in range(M):
    L.append(input())
    
for i in L:
    print(memo[i])