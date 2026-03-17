import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
L = [0] + L
M = int(input())
tree = [float('inf')]*(4*N)
def build(node,start,end):
    if start ==end:
        tree[node] = start
        return
    mid = (start+end)//2
    build(node*2,start,mid)
    build(node*2+1,mid+1,end)
    if L[tree[node*2]] > L[tree[node*2+1]]:
        tree[node] = tree[node*2+1]
    else:
        tree[node] = tree[node*2]

def ask(node,start,end,left,right):
    if start >  right or left >  end:
        return -1
    if start >=left and right>=end:
        return tree[node]

    mid = (start+end)//2
    left_min = ask(node*2,start,mid,left,right)
    right_min = ask(node*2+1,mid+1,end,left,right)
    if left_min == -1:
        return right_min
    if right_min == -1:
        return left_min
    if L[left_min] > L[right_min]:
        return right_min
    else:
        return left_min


def update (node,start,end,target_index,real_num):#
    if start == end:
        if start == target_index:
            L[target_index] = real_num
        tree[node] = target_index
        return
    if start<=target_index<=end:
        mid = (start+end)//2
        if start<=target_index<=mid:
            update(node*2,start,mid,target_index,real_num)
        else: 
            update(node*2+1,mid+1,end,target_index,real_num)

        if L[tree[node*2]] > L[tree[node*2+1]]:
            tree[node] = tree[node*2+1]
        else:
            tree[node] = tree[node*2]
    


build(1,1,N)
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 2:
        print(ask(1,1,N,b,c))
    else:
        update(1,1,N,b,c)