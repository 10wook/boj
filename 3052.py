L = []
for i in range(10):
    a = int(input())
    L.append(a%42)
print(len(set(L)))