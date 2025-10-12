N,M = map(int, input().split())
L = list(map(int,input().split()))
L.sort()
import itertools
a= list(set(itertools.combinations_with_replacement(L,M)))
a = sorted(a)
for i in a:
    for j in i:
        print(j,end=' ')
    print('')