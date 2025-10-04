N = int(input())
def fac(i:int):
    if i <= 1:
        return 1
    else: 
        return fac(i-1)*i
print(fac(N))