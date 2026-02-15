def turn(num):
    if num ==0:
        return 1
    else:
        return 0
N = int(input())
switchs = [-1]+list(map(int,input().split()))
M = int(input())
for _ in range(M):
    sex,num = map(int,input().split())
    if sex == 1:
        for i in range(num,N+1,num):
            switchs[i] = turn(switchs[i])
    else:
        check = 1
        switchs[num] = turn(switchs[num])
        while num +check <=N and num-check>=1:
            if switchs[num-check]!=switchs[num+check]:
                break
            else:
                switchs[num-check] = turn(switchs[num-check])
                switchs[num+check] = turn(switchs[num+check])
                check+=1
                
for i in range(1,N+1):
    if i%20==0:
        print(switchs[i])
    else:
        print(switchs[i],end=' ')