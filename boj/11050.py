N, M = map(int,input().split())

import itertools
# print(itertools.combinations(range(N),M))
cnt = 0
for i in itertools.combinations(range(N),M):
    cnt +=1
    # print(i)
# print(len())
print(cnt)