import sys
input = sys.stdin.readline
N, M = map(int,input().split())
def build(node,start,end):
    if start ==end:
        tree[node] = numbers[start]
    else:
        mid = (start+end)//2
        build(node*2,start,mid)
        build(node*2+1,mid+1,end)
        tree[node] = min(tree[node*2],tree[node*2+1])
numbers = [int(input())for _ in range(N)]
tree = [0]*(4*N)
build(1,0,N-1)
# print(tree)
def minimun(node,start,end,left,right):
    if start > right or end < left:
        return float('inf')
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    return min(minimun(node*2,start,mid,left,right),minimun(node*2+1,mid+1,end,left,right))
 

# print(tree,numbers)
for _ in range(M):
    a,b = map(int,input().split())
    print(minimun(1,0,N-1,a-1,b-1))
