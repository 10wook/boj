tot = int(input())
S,M,L,XL,XXL,XXXL = map(int,input().split())
T,P = map(int,input().split())
T_cnt = 0
TL =  [S,M,L,XL,XXL,XXXL]

for i in TL :
    T_cnt += i//T
    if i%T > 0:
        T_cnt += 1
        
        
print(T_cnt)
print(tot//P,tot%P)
    