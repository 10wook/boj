N = int(input())

import math
fiac = math.factorial(N)

# print(fiac)
cnt = 0 
while True:
    if fiac%10 ==0:
        cnt +=1
        fiac=fiac//10
    else:
        break
print(cnt)