num = int(input())
for i in range(1,num+1,1):
    print(" " * ((2*num - 1-(2 * i - 1))//2) + "*" * (2 * i - 1)  )
for i in range(num-1, 0, -1):
    print(" " * ((2*num - 1-(2 * i - 1))//2) + "*" * (2 * i - 1) )