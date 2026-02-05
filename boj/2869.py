D, N, L = map(int,input().split())
import math
cnt = math.ceil((L-D)/(D-N))

print(cnt+1)