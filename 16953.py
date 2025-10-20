N,M = map(int,input().split())

def plus_one(n:int):
    return n*10+1
def multiple(n:int):
    return n*2


from collections import deque


queue = deque([(N, 1)])  # (현재값, 연산횟수)

while queue:
    num, cnt = queue.popleft()
    if num == M:
        print(cnt)
        break
    elif num < M:
        queue.append((plus_one(num), cnt + 1))
        queue.append((multiple(num), cnt + 1))
else:
    print(-1)
