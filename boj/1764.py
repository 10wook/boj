import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dude = set()
for i in range(N):
    dude.add(input())
bojap = []    
for i in range(M):
    a = input()
    if a in dude:
        bojap.append(a)
        
print(len(bojap))
bojap.sort()
# print(bojap)
for i in bojap:
    print(i,end='')
        
    