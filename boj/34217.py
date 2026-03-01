A2, B2 = map(int,input().split())
A1,B1 =  map(int,input().split())
if A1+A2 < B1+B2 :
    print('Hanyang Univ.')
elif A1+A2 > B1+B2 :
    print('Yongdap')
else:
    print('Either')