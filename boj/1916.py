import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

# 인접 딕셔너리: Bus[u][v] = u->v 간선의 최소 비용
Bus = {}
for _ in range(M):
    u, v, w = map(int, input().split())
    if u not in Bus:
        Bus[u] = {}
    # 같은 간선이 여러 번 있을 수 있으므로 최소값만 저장
    Bus[u][v] = min(Bus[u].get(v, float('inf')), w)

start, end = map(int, input().split())

INF = 10**18
dist = [INF] * (N + 1)
dist[start] = 0

pq = [(0, start)]  # (현재비용, 노드)

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue  # 이미 더 좋은 경로로 갱신된 경우 스킵

    # u에서 나가는 간선이 없을 수도 있으니 .get 사용
    for v, w in Bus.get(u, {}).items():
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

print(dist[end])