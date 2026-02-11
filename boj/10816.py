N = int(input())
dict = {}
for i in list(map(int,input().split())):
    if dict.get(i):
        dict[i] +=1
    else:
        dict[i] = 1
M= int(input())
for i in  list(map(int,input().split())):
    if dict.get(i):
        print(dict[i], end = ' ')
    else:
        print(0,end=' ')
