import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nlist = [0]*(N+1)
tree = [0]*(4*N)

#기본적인 트리 조회는 시작,끝 합을 담고 잇는 애를 알게 된다. 
def modify(node,diff,start,end,index):
    #내 차이를 인정하고, 그만큼 수정해 나가면서.. 수정
    if index <start or index >end: #만약 범위에서 벗어났다면 아무것도 안한다.
        return
    # 일단 들어왔다?
    # 바로 일단 수정
    tree[node] = tree[node] +diff
    if start !=end:
        mid = (start+end)//2
        modify(node*2,diff,start,mid,index)
        modify(node*2+1,diff,mid+1,end,index)
    pass

#left,right는 입력 받은(합을 구해야할 왼쪽,오른쪽)
# 여기가 포함할 값의 범위
def Sum (node,start,end,left,right):
    if right < start or left > end:
        return 0
    if left <=start and end<=right:
        return tree[node]
    mid = (start+end)//2
    return Sum(node*2,start,mid,left,right) + Sum(node*2+1,mid+1,end,left,right)

ans = []

for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 0:
        if b > c:
            b, c = c, b
        ans.append(str(Sum(1, 1, N, b, c)))
        pass
    else:
        diff = c - nlist[b]#새로 추가된 값을 계산 해준다. 모든 노드에 대해서 이걸 더해주면 된다.
        nlist[b] = c
        modify(1,diff,1,N,b)
print('\n'.join(ans))