N = int(input())
l = []
for i in range(N):
    a,b = input().split()
    l.append([int(a),b])
    
    
for i in range(1,201):
    for p in l:
        if p[0] == i:
            print(p[0],p[1])