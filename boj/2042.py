import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N) ]
tree = [0]*(4*N)
#맨 앞에 가장 큰 총합이 들어있고, (트리를 구성한다. *2,*2+1을 활용해서 숫자 설정)
def build(node,start,end):
    if start ==end:
        tree[node]=arr[start]
        return
    mid = (start+end)//2
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)
    tree[node] = tree[node*2]+tree[node*2+1]
def query(node,start,end,left,right):
    if right < start or left > end:
        return 0
    if left <=start and end<=right:
        return tree[node]
    mid = (start+end)//2
    return query(node*2,start,mid,left,right)+query(node*2+1,mid+1,end,left,right)

def update(node,start,end,index,diff):
    if index <start or index >end:
        return
    tree[node]+=diff
    if start!=end:
        mid = (start+end)//2
        update(node*2,start,mid,index,diff)
        update(node*2+1,mid+1,end,index,diff)

build(1,0,N-1)
for i in range(M+K):
    a,b,c = map(int,input().split())
    if a ==1:
        b-=1
        diff = c - arr[b]
        arr[b] = c
        update(1,0,N-1,b,diff)
        pass
    else:
        b -= 1
        c -= 1
        print(query(1, 0, N - 1, b, c))
        pass