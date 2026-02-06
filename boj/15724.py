import sys
input = sys.stdin.readline

N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(list(map(int,input().split())))    
# L은 N*N크기의 행렬입니다

#여기서 2차원 누적합을 구해줍니다.
prefix = [[0]*(M+1) for _ in range(N+1)]

#2차원 배열 채우기
for i in range(1,N+1):
    for j in range(1,M+1):
        prefix[i][j] = L[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
# print(prefix)
K = int(input())
for _ in range(K) : 
    x1,y1,x2,y2 = map(int,input().split())
    #앞에 주어지는 애들이 무조건 작고, 지금의 경우에는 누적합에는 입력갑 그대로 계산해주면 되고, 뺄 친구는 -1씩 해준애로 계산하면 된다. 
    # 2차원 누적합 기본 공식은 포함 배제의 원래를 이용해서 pre[x2][y2] + pre[x1-1][y1-1] - pre[x2][y1-1]- pre[x1-1][y2]
    print(prefix[x2][y2] + prefix[x1-1][y1-1] - prefix[x2][y1-1]- prefix[x1-1][y2])

