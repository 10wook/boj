L= []
while (True):
    N = float(input())
    if N == 0:
        break
    L.append(N)
cnt = 0
for i in L:
    cnt += i
print (cnt/len(L))    