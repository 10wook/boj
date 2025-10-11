N, M = map(int,input().split())
import itertools

for i in itertools.combinations(range(1,N+1),M):
    for j in i:
        print(j,end=' ')
    print('')