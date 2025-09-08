# 삼성 문제 퇴사
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N) :
    p,t = map(int,input().split())
    arr.append([p,t])


dpList = [0]*(N)

for i in range(1,N+1) :
    k = N-i
    if k==N-1 :
        if k+arr[k][0] <= N :
            dpList[k] = arr[k][1]
    elif k +arr[k][0] >N :
        dpList[k] = dpList[k+1]
    else :
        if k+arr[k][0] < N :
            dpList[k] = max(dpList[k+1],arr[k][1]+dpList[k+arr[k][0]])
        elif k+arr[k][0] >=N:
            dpList[k] = max(dpList[k+1],arr[k][1])
#     print(dpList)
print(max(dpList))



print()