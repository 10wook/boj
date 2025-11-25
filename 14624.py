N= int(input())
A = N -1
B = 1
if N%2 ==0:
    print('I LOVE CBNU')
else:
    for i in range((N//2)+2):
        if i == 0 :
            print('*'*N)
        elif i == 1:
            print(' '*(N//2),end='')
            print('*')
        else:
            print(' '*(N//2-(i-1)),end='') 
            print('*',end='')
            print(' '*(-3+(2*i)),end='') # 2를 넣으면 1이 나와야함
            print('*')
            
            
            
# print('''*******
#    *
#   * *
#  *   *
# *     *''')