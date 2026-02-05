T = int(input())
def find_max(L:list):
    M = L[0]
    for i in L:
        if i > M:
            M = i
    return M
def find_min(L:list):
    M = L[0]
    for i in L:
        if i < M:
            M = i
    return M
for test_num in range(1, T + 1):
    length = int(input())
    L = list(map(int,input().split()))
    answer = []
    for i in range(5):
        answer.append(find_max(L))
        answer.append(find_min(L))
        L.remove(find_min(L))
        L.remove(find_max(L))
    print(f'#{test_num}',*answer)
            