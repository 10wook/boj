T = int(input())
for i in range(1,T+1):
    len =int(input())
    L = list(map(int,input().split()))

    mi = min(L)
    ma = max(L)
    max_in = 0
    for j in range(len-1,-1,-1):
        if L[j] ==ma:
            max_in = j
            break
    
    print(f'#{i} { abs(max_in-L.index(mi)) }')