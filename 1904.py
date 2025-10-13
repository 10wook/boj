N = int(input())
a = 1
b = 2
for i in range(2,N):
    temp = (a +b)%15746
    a =b
    b = temp

if N == 1:
    print(1)
elif N ==2 :
    print(2)
else:
    print(b%15746)