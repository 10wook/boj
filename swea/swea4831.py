T = int(input())

def greedy (curr,K):
    global CS
    # print(CS)
    L  = []
    for i in CS:
        if i <= curr+K:
            L.append(i)
    return L[-1]

    pass
for i in range(1,T+1):
    K,N,M = map(int,input().split())
    # K 한번 충전시 이동가능
    # N  종점 번호
    # M 충전소 갯수
    CS = list(map(int,input().split())) + [N]
    answer = -1
    curr = 0
    far = curr + K
    # CS안에서 가장 멀리 갈 수 있는 만큼 가고, 그걸 취득함
    while True:
        answer+=1
        curr_dest = greedy(curr,K)
        
        
        if curr_dest ==curr:
            answer = 0
            break
        curr = curr_dest
        if curr >= N:
            break 
    print(f'#{i} {answer}')