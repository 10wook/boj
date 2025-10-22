import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
M = int(input())

Bus = {}
for _ in range(E):
    u, v, w = map(int, input().split())
    if u not in Bus:
        Bus[u] = {}
    Bus[u][v] = min(Bus[u].get(v, float('inf')), w)

INF = float('inf')

def dijkstra(start):
    distance = [INF] * (V + 1)
    distance[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        # 이미 더 짧은 거리로 방문된 경우 스킵
        if curr_dist > distance[curr_node]:
            continue

        if curr_node not in Bus:
            continue

        for next_node, weight in Bus[curr_node].items():
            new_dist = curr_dist + weight
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return distance

distances = dijkstra(M)

for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
