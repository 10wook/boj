num = int(input())
L = []
for i in range (num):
    L.append(list(input().split()))
for i in L:
    i[0]=int(i[0])
    output = ''
    for j in i[1]:
       output = output+(j*i[0])
    print(output)