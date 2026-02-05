import sys
sys.setrecursionlimit(10**6)
N = int(input())
Graph = {}
for i in range(N-1):
    a,b = map(int,input().split())
    if a in Graph:
        Graph[a].add(b)
    else:
        Graph[a] = {b}
    if b in Graph:
        Graph[b].add(a)
    else:
        Graph[b] = {a}
        
parents=dict()  
parents[1] = 0   
def DFS(node, parent):
    for nxt in Graph[node]:
        if nxt != parent:  # 부모로 역방문 방지
            parents[nxt] = node
            DFS(nxt, node)
visited = {i}
    
DFS(1,0)
for i in range(2,N+1):
    print(parents[i])
