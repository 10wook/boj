T = int(input())
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,T+1):
    N = int(input())
    visited = set()
    queue = deque()
    maze = [input() for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2': 
                visited.add((i,j))
                queue.append((i,j,0))
    while queue:
        x,y,moves = queue.popleft()
        visited.add((x,y))
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N and not (x+dx[i],y+dy[i]) in visited:
                if maze[x+dx[i]][y+dy[i]] =='3':

                    check = True
                    break
                elif maze[x+dx[i]][y+dy[i]] =='0':
                    # 추가
                    queue.append((x+dx[i],y+dy[i],moves+1))
        if check:
            break

    if check:
        print(f"#{test_num} {moves}")
    else:
        print(f"#{test_num} {0}")