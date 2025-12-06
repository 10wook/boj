N,M = input().split()
RN=''
for c in N:
    RN = c + RN

RM=''
for c in M:
    RM = c + RM
    
RM = int(RM)
RN = int(RN)
if RM <= RN:
    print(RN)
else:
    print(RM)