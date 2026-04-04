A = input()
N = int(input())
cnt = 0
for _ in range(N):
    temp = input()
    if A[:5] == temp[:5]:
        cnt+=1
print (cnt)