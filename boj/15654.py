N,M = map(int, input().split())
L = list(map(int,input().split()))
L.sort()
import itertools
for i in itertools.permutations(L,M):
    for j in i:
        print(j,end=' ')
    print('')