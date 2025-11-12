N = list(input())
N.sort()
for i in range(len(N)-1,-1,-1):
    print(N[i],end='')