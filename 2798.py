N, M = map(int, input().split())
L = input().split()
for i in range(N):
    L[i] = int(L[i])
totC = []
import itertools
for i in  itertools.combinations(L,3):
    cnt = 0
    for j in i:
        cnt+=j
    if cnt <= M:
        totC.append(cnt)
print(max(totC))

# print(C)