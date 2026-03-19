import sys
input = sys.stdin.readline
def build(node,start,end): #(짝수,홀수)
    if start ==end:
        if L[start]%2 ==0:
           tree[node] = (1,0)
        else:
           tree[node] = (0,1)
        return
    mid = (start+end)//2
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)
    tree[node] = (tree[node*2][0]+tree[node*2+1][0],tree[node*2][1]+tree[node*2+1][1])
def ask(node,start,end,left,right):
    if  right < start or left > end:
        return (0,0)
    if right >= end and left <= start:
            return tree[node] 
    mid = (start+end)//2
    a = ask(node*2,start,mid,left,right)
    b = ask(node*2+1,mid+1,end,left,right)
    return (a[0]+b[0],a[1]+b[1])
def change(node,start,end,target_node,even:bool):#내려가면서 짝수 홀수만 바꾸어주면 되자나~~
    if start ==end == target_node:
        if even:
            tree[node] = (1,0)
        else:
            tree[node] = (0,1)
        return
    mid = (start+end)//2
    
    if target_node <= mid:
        change(node*2,start,mid,target_node,even)
    else:
        change(node*2+1,mid+1,end,target_node,even)
    
    tree[node] = (
        tree[node*2][0] + tree[node*2+1][0],
        tree[node*2][1] + tree[node*2+1][1]
    )
    
    
N = int(input())
L = list(map(int,input().split()))
tree = [(0,0)] * (4*N)
M = int(input())
build(1,0,N-1)
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        if L[b-1] % 2 != c % 2:
            if c % 2 == 0:
                change(1,0,N-1,b-1,True)
            else:
                change(1,0,N-1,b-1,False)
        L[b-1] = c
    elif a == 2 :
        print(ask(1,0,N-1,b-1,c-1)[0])
    else:
        print(ask(1,0,N-1,b-1,c-1)[1])
        