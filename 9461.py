N = int(input())


P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
def padovan(N : int):
    if N < len(P):
        return P[N]
    else:
        for i in range(len(P),N+1):
           P.append(P[i-1]+P[i-5])
        
    return(P[N])

for i in range(N):
    
    print(padovan(int(input())))
