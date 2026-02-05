N,M = map(int,input().split())
from itertools import product

for i in product(range(1,N+1),repeat= M):
    for j in i:
        print(j,end=' ')
    print()
    