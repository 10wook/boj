N = int(input())
L =[]
for i in range(N):
    a,b = map(int,input().split())
    L.append([a,b])
    
L.sort(key=lambda i :(i[0], i[1]))

for i in L :
    print(i[0],i[1])