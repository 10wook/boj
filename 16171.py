S = input()
K=input()
a =''

for i in S:
    if i.isalpha():
        if a =='':
            a = i
        else:
            a = a + i
            
            
# print(a)
if K in a:
    print(1)
else:
    print(0)