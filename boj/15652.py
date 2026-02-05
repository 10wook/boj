N,M = map(int, input().split())
import itertools
for i in itertools.combinations_with_replacement(range(1,N+1),M):
    for j in i:
        print(j,end=' ')
    print('')