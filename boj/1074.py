N, r, c = map(int,input().split())
def Z(N,r,c):
    N = N-1
    if (2**N - r) <= 0 and (2**N - c) <= 0:
         return Z(N,r-2**N,c-2**N)+((2**N)**2)*3
    if (2**N - r) <= 0 and (2**N - c) > 0:
        return Z(N,r-2**N,c)+((2**N)**2)*2
    if (2**N - r) > 0 and (2**N - c) <= 0:
        return Z(N,r,c-2**N)+((2**N)**2)*1
    if (2**N - r) > 0 and (2**N - c) > 0:
        if N<1:
            if r==0 and c==0:
                return 0
            if r==0 and c==1:
                return 1
            if r==1 and c==0:
                return 2
            if r==1 and c==1:
                return 3
        else:
            return Z(N,r,c)


print(Z(N,r,c))