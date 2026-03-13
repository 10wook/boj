import sys
input = sys.stdin.readline

MOD = 1000000007

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

tree = [1] * (4 * N)

def build(node, start, end):
    if start == end:
        tree[node] = numbers[start] % MOD
        return
    
    mid = (start + end) // 2
    build(node*2, start, mid)
    build(node*2+1, mid+1, end)
    
    tree[node] = (tree[node*2] * tree[node*2+1]) % MOD


def mul_all(node, start, end, left, right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    return (mul_all(node*2, start, mid, left, right) *
            mul_all(node*2+1, mid+1, end, left, right)) % MOD


def update(node, start, end, index, value):
    if start == end:
        tree[node] = value % MOD
        return
    
    mid = (start + end) // 2
    
    if index <= mid:
        update(node*2, start, mid, index, value)
    else:
        update(node*2+1, mid+1, end, index, value)
    
    tree[node] = (tree[node*2] * tree[node*2+1]) % MOD


build(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        numbers[b-1] = c
        update(1, 0, N-1, b-1, c)
    else:
        print(mul_all(1, 0, N-1, b-1, c-1))