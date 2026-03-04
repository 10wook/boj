from collections import deque
T = int(input())

for test_num in range(1,T+1):
    answer = 0
    queue = deque()
    visited = set()
    
    curr,target = map(int,input().split())
    queue.append((curr,0))
    visited.add(curr)
    while queue:
        curr,answer = queue.popleft()

        if curr == target:
            print(f'#{test_num} {answer}')
            break
        if 0<=curr*2 <= 1000000 and not (curr*2 in visited):
            queue.append((curr*2,answer+1))
            visited.add(curr*2)
        if 0<=curr +1 <=1000000 and not (curr+1 in visited):
            queue.append((curr+1,answer+1))
            visited.add(curr+1)
        if curr-1>=0 and not curr-1 in visited:
            queue.append((curr-1,answer+1))
            visited.add(curr-1)
        if curr-10>=0 and not curr-10 in visited:
            queue.append((curr-10,answer+1))
            visited.add(curr-10)
        
        ## 디큐 공부해야합니다....
        #활용형 처럼..