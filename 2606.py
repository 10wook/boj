N = int(input())
M = int(input())
D ={}
for i in range(1,N+1):
    D[i] = set()
    
for i in range(M):
    a,b = map (int,input().split())
    D[a].add(b)
    D[b].add(a)

#연결 확인 하는 함수
# 재귀로 구현
S = set()
L = []
def worm(index:int):
    # print(index)
    S.add(index)
    for i in D[index]:
        if i in S: #만약 이미 조회가 된 아이라면...
            pass
        else: #만약 조회가 안되었다면?
            S.add(i)
            for j in D[i]:
                if j not in S:
                    S.add(i)
                    worm(j)
    pass
worm(1)

print(len(S)-1)
