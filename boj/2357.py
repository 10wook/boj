import sys
input = sys.stdin.readline
N,M = map(int, input().split())
L = [int(input()) for _ in range(N)]
tree = [(float('inf'),-float('inf'))]*(4*N)
#(min max)형태로 저장할겁니다.
def build(node,start,end):
    if start == end:
        tree[node] = (L[start],L[start])
    else:
        mid = (start+end)//2
        build(node*2,start,mid)
        build(node*2+1,mid+1,end)
        tree[node] = (min(tree[node*2][0],tree[node*2+1][0]),max(tree[node*2][1],tree[node*2+1][1]))
    return 
def ask (node,start,end,left,right):
    if start > right or end < left:
        return (float('inf'),-float('inf'))
    if start >= left and right >= end:
        return (tree[node])
    mid = (start+end)//2
    left_node = ask(node*2,start,mid,left,right)
    right_node = ask(node*2+1,mid+1,end,left,right)
    return (min(left_node[0],right_node[0]),max(left_node[1],right_node[1]))

build(1,0,N-1)
# print(tree)
for _ in range(M):
    a,b = map(int,input().split())
    answer = ask(1,0,N-1,a-1,b-1)
    print(answer[0],answer[1])