L = []
while True:
    try:
        L.append(input())
    except EOFError:
        break

for j in range(15):
        for i in L:
            if len(i)> j :
                print(i[j],end='')
                
                