S = input()
s = set()
for i in range(len(S)):
    for j in range(len(S)):
        if len(S) >= (i + j):
            s.add(S[j:j+i])
            
print (s)
print(len(s))