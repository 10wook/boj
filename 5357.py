N = int(input())
for i in range(N):
    a = input()
    x = ''
    for j in a:
        if x != j:
            print(j,end='')
            x=j
    print('')