T = int (input())
for i in range(1,T+1):
    N = int(input())
    L = []
    buses = {}
    for j in range(N):
       S, D = map(int,input().split())
       for k in range(S,D+1):
            if buses.get(k):
               buses[k] +=1
            else:
               buses[k] = 1
    #여기서 버스 정류장 별로 지나가는 버스를 모두 추가해준다.
    P = int(input())
    answer = []
    for j in range(P):
        answer.append(int(input()))

    print(f'#{i}',end =' ')
    for j in answer:
        if buses.get(j):
            print(buses[j], end =' ')
        else:
            print(0,end =' ')
    if i ==T:
        pass
    else:
        print()

    

    #딕셔너리에서 없는 경우 문제가 발색하니까 유의하기