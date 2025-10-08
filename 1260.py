N,M,V = map(int,input().split())
Edge = {i: [] for i in range(1, N+1)}  
for i in range(M):
    s,e = map(int,input().split())
    if s in Edge:
        Edge[s].append(e)
    else:
        Edge[s] = [e]
    if e in Edge:
            Edge[e].append(s)
    else:
        Edge[e] = [s]
        
for i in Edge:
    Edge[i].sort()
    
# print(Edge)
passed = set()
def DFS(V):
    print(V, end=' ')
    passed.add(V)
    for i in Edge[V]:
        if i not in passed:
            DFS(i)
            
            
from collections import deque

def BFS(V):
    queue = deque([V])
    visited = set([V])
    order = []
    
    while queue:
        curr = queue.popleft()
        order.append(curr)
        for i in Edge[curr]:
            if i not in visited:
                visited.add(i)
                queue.append(i)
    return order

DFS(V)
print('')
passed = set()
passed.add(V)
a = BFS(V)
for i in a:
    
    print(i,end=' ')