import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
L = [0]+L
tree = [0]*(4*N)
def build(node,start,end):
    if start == end :
        tree[node] = L[start]
        return
    else:
        mid = (start+end)//2
        build(node*2,start,mid)
        build(node*2+1,mid+1,end)
        tree[node] = min(tree[node*2],tree[node*2+1])
        return

def ask(node,start,end,left,right):
    if start > right or end < left:
        return float('inf')
    if left <= start and right >= end:
        return tree[node]
    mid = (start+end)//2
    return min(ask(node*2,start,mid,left,right),ask(node*2+1,mid+1,end,left,right))
def update(node,start,end,target_node,new_num):
    if start==end==target_node:
        tree[node] = new_num
        return
    mid = (start+end)//2
    if mid >= target_node:
        update(node*2,start,mid,target_node,new_num)
    else:
        update(node*2+1,mid+1,end,target_node,new_num)
    tree[node] = min(tree[node*2],tree[node*2+1])

build(1,1,N)
M = int(input())
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        update(1,1,N,b,c)
    else:
        print(ask(1,1,N,b,c))