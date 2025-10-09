N = int(input())
for i in range(N):
    a,b = input().split()
    cnt = 0
    if len(a) ==len(b):
        if a==b:
            print('OK')
        else:
            print("ERROR")
    else:
        print("ERROR")