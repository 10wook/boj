import math
D,N,M = map(int,input().split())
k = D / math.sqrt(N**2 + M**2)
real_height = int(math.floor(N * k))
real_width = int(math.floor(M * k))

print(real_height, real_width)