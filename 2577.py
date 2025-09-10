A = int(input())
B = int(input())
C = int(input())
ABC = A*B*C
L = [0,0,0,0,0,0,0,0,0,0]
while ABC != 0 :
    L[ABC%10] = L[ABC%10]+1
    ABC = ABC//10
    
for i in L:
    print(i)