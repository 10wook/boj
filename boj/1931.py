N = int(input())
L = []
for i in range(N):
    L.append(list(map(int,input().split())))
    

L = sorted(L, key=lambda x: x[1], reverse=False)
# print(L)

L.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0
for s, e in L:
    if s >= end_time:   # 직전 회의 끝난 뒤 시작할 수 있으면
        cnt += 1
        end_time = e

print(cnt)