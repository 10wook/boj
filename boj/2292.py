N = int(input())
import math
if N ==1 :
    print (1)
else:
    i = 0
    while True:
        if N <= 1:
                break
        # print( 6 *i)
        N -= 6 *i

        i +=1
    print (i)