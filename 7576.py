import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Ts = []
for i in range(M):
    Ts.append(input().split())

for i in range(M):
    for j in range(N):
        Ts[i][j]=int(Ts[i][j])
# print(Ts)


def totdays(Ts):
    NTs = [row[:] for row in Ts]
    changed = False
    for i in range(M):
        for j in range(N):
            if Ts[i][j] == 1:
                # 좌
                if j > 0 and Ts[i][j-1] == 0:
                    NTs[i][j-1] = 1; changed = True
                # 상
                if i > 0 and Ts[i-1][j] == 0:
                    NTs[i-1][j] = 1; changed = True
                # 우
                if j < N-1 and Ts[i][j+1] == 0:
                    NTs[i][j+1] = 1; changed = True
                # 하
                if i < M-1 and Ts[i+1][j] == 0:
                    NTs[i+1][j] = 1; changed = True
    return NTs, changed

def all_done(Ts):
    for i in range(M):
        for j in range(N):
            if Ts[i][j] == 0:
                return False
    return True



days = 0
while True:
    if all_done(Ts):
            break
    NTs, changed = totdays(Ts)
    if not changed:
        days = -1
        break
    Ts = NTs
    days += 1

print(days)