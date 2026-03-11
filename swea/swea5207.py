
def binary_search(target):
    
    l = 0
    r = N-1
    
    last = 0   # 0: 없음, 1: left, 2: right
    
    while l <= r:
        
        m = (l+r)//2
        
        if A[m] == target:
            return True
        
        elif A[m] > target:
            if last == 1:
                return False
            r = m-1
            last = 1
        
        else:
            if last == 2:
                return False
            l = m+1
            last = 2
    
    return False


T = int(input())

for t in range(1, T+1):
    
    N, M = map(int,input().split())
    
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    A.sort()
    
    cnt = 0
    
    for x in B:
        if binary_search(x):
            cnt += 1
    
    print(f'#{t} {cnt}')