import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    cnt = 0
    
    for _ in range(N):
        v, f, c = map(int, input().split())
        
        # 연료 충분 조건: f * v >= D * c
        if f * v >= D * c:
            cnt += 1
    
    print(cnt)
