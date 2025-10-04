import sys
input = sys.stdin.readline
N,H = map(int, input().split())
L0 ={}
L1 = {}
for i in range(N):
    a = int(input())
    if i%2 ==0:
        if a in L0:
            L0[a]=L0[a]+1
        else:
            L0[a]=1
    else:
        if a in L1:
            L1[a]=L1[a]+1
        else:
            L1[a]=1

a= 1
min_cnt = N+1
mins_cnt = 0
while True:
    if a >= H:
        break
    cnt = 0
    # 석순: 길이 >= a
    for i in range(a, H+1):
        if i in L0:
            cnt += L0[i]

    # 종유석: 길이 >= H-a+1
    for i in range(H-a+1, H+1):
        if i in L1:
            cnt += L1[i]

    if min_cnt == cnt:
        mins_cnt+=1
    elif min_cnt > cnt :
        mins_cnt = 1
        min_cnt = cnt
    
    a +=1
    
    
print(min_cnt,mins_cnt)

        
        
        
