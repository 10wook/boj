N = int(input())
import statistics
L =[]
for i in range(N):
    L.append(int(input()))
print(statistics.mean(L))
print(statistics.median(L))
print(statistics.mode(L))
print(max(L)-min(L))