N = int(input())
M = input()
# print(M)
cnt = 0
for i in range(len(M)):
    cnt += (ord(M[i])-96)*(31**i) 
print(cnt%1234567891)