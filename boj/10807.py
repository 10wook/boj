N = int (input())
L = input().split()
M = input()
cnt = 0
for i in L :
    if i ==M:
        cnt+=1
print (cnt)