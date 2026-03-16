import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((c, b))   # (가중치, 정점)
    G[b].append((c, a))

visited = [False] * (V + 1)
pq = [(0, 1)]   # (비용, 시작정점)
answer = 0

while pq:
    cost, node = heapq.heappop(pq)

    if visited[node]:
        continue

    visited[node] = True
    answer += cost

    for next_cost, next_node in G[node]:
        if not visited[next_node]:
            heapq.heappush(pq, (next_cost, next_node))

print(answer)