A, B, C = map(int,input().split())
def change(A,B,C):
    if A+B < C:
        return 0
    else:
        new = (A+B)//C
        left = (A+B)%C
        return change(left,new,C) + new
    
    
print(change(A,B,C))