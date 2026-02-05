L = input().split()
cnt = 0
for i in range(len(L)):
    cnt = cnt + int(L[i])*int(L[i])
print(cnt%10)