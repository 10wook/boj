import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) 
N, M =map(int, input().split())
L = []
for i in range(N):
    L.append(list(map(int,input().split())))
    
    
checked = set()
#1. 내가 1인 위치들 조회.
#2. 만약 1이면 전방위를 돌면서 조회 안된 애들 세어서 추가 => DFS함수로 구현
def DFS(r,c):
    if (r,c) in checked:
        return 0
    if L[r][c] != 1 :
            return 0
    else:
        size = 0
        checked.add((r,c))
        if L[r][c] ==1 :
            size+=1
        
            
            #전 방위를 돌아보면서 시도 ㄱㄱ
            if r > 0:
                size += DFS(r-1,c)
            if r < N-1:
                size += DFS(r+1,c)
            if c > 0:
                size += DFS(r,c-1)
            if c < M-1:
                size += DFS(r,c+1)
    return size



#3. 다음 애들 돌면서 확인한다. -> 만약 이미 조회한 애면 넘어갈것,
curr = 0
bigest = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if L[i][j] ==1 and (i,j) not in checked:
            cnt +=1
            curr = DFS(i,j)
            if bigest < curr:
                big = bigest
                bigest =curr

                
#4. max로 조회하면서 돌것
print(cnt)
print(bigest)

