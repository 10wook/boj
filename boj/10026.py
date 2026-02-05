import sys
sys.setrecursionlimit(2000000)

N = int(input())

painting = []
for i in range(N):
    painting.append(input())
    
visited = set()
#DFS를 돌면서 한그룹이 있다는 걸 어떻게 표현하지...
index = 0
#만약 인덱스가 0 아 아니면 cnt를 추가하자
def DFS(r,c,index):
    color = painting[r][c]
    if (r,c) not in visited:
        visited.add((r,c))
        if r > 0 and painting[r-1][c]==color:
            index += DFS(r-1,c,index)
        if r < N-1 and painting[r+1][c]==color:
            index +=DFS(r+1,c,index)
        if c > 0 and painting[r][c-1]==color:
            index +=DFS(r,c-1,index)
        if c < N-1 and painting[r][c+1]==color:
            index +=DFS(r,c+1,index)      
        index+=1
    # print(index)
    return(index)


cnt = 0
for i in range(N):
    for j in range(N):
        index = 0
        index = DFS(i,j,index)
        if index!=0:
            cnt +=1
print(cnt,end= ' ')


visited = set()

for i in range(N):
    painting[i] = painting[i].replace('R','G')
        
cnt = 0       
for i in range(N):
    for j in range(N):
        index = 0
        index = DFS(i,j,index)
        if index!=0:
            cnt +=1
print(cnt)