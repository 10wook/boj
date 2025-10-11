import sys
    
    
def build_prev_next(arr):
    n = len(arr)
    prev = [-1] * n
    next = [n] * n
    last_seen = {}

    for i, v in enumerate(arr):
        if v in last_seen:
            prev[i] = last_seen[v]
        last_seen[v] = i

    last_seen.clear()

    for i in range(n-1, -1, -1):
        v = arr[i]
        if v in last_seen:
            next[i] = last_seen[v]
        last_seen[v] = i

    return prev, next

def find_pivot(l, r, prev, next):
    # 양쪽 끝부터 안쪽으로 좁혀가며 탐색 (효율적)
    i, j = l, r
    while i <= j:
        if prev[i] < l and next[i] > r:
            return i
        if prev[j] < l and next[j] > r:
            return j
        i += 1
        j -= 1
    return -1  # 못 찾으면 boring
def is_non_boring(l, r, prev, next):
    # 종료 조건: 구간 길이 1 이하면 무조건 non-boring
    if l >= r:
        return True

    i, j = l, r
    while i <= j:
        # 왼쪽에서 고유값 중심 찾기
        if prev[i] < l and next[i] > r:
            return (
                is_non_boring(l, i - 1, prev, next) and
                is_non_boring(i + 1, r, prev, next)
            )
        # 오른쪽에서 고유값 중심 찾기
        if prev[j] < l and next[j] > r:
            return (
                is_non_boring(l, j - 1, prev, next) and
                is_non_boring(j + 1, r, prev, next)
            )
        i += 1
        j -= 1
    
    # 고유값 중심을 못 찾으면 boring
    return False

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(input())  # 테스트케이스 수
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    prev, next = build_prev_next(arr)
    result = is_non_boring(0, len(arr)-1, prev, next)
    print("non-boring" if result else "boring")
    
    
