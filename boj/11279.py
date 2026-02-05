import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if heap:
            # 가장 큰 값 = 가장 작은 음수의 부호를 다시 뒤집어서 출력
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        # 최대 힙처럼 쓰기 위해 음수로 저장
        heapq.heappush(heap, -a)