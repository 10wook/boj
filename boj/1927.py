import heapq
import sys
input = sys.stdin.readline
H = []

N = int(input())
for i in range(N):
    query = int(input())
    if query ==0:
        if len(H)==0:
            print(0)
        else:
             print(heapq.heappop(H))
    else:
        heapq.heappush(H, query)