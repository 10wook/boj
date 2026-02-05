N = int(input())
L = input().split()
cnt = 0

def prime_check(N):
    for i in range(2,N):
        if N%i ==0:
            return False
    return True
        
cnt = 0
for i in L:
    if int(i) ==1:
        pass
    else:
        if prime_check(int(i)):
            cnt+=1
            
print(cnt)