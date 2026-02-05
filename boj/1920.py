N = int(input())
L = set(input().split())
N = int(input())
L2 = input().split()
for i in L2:
    if i in L:
        print(1)
    else:
        print(0)