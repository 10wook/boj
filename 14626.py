num = input()
star = num.find('*')
# print(star)
cnt = 0
for i in range(13):
    if num[i] != "*":
        if i%2 ==0:
            cnt+=int(num[i])
        else: 
            cnt+=(int(num[i])*3)
       
if star%2 ==0:
    for i in range(10):
        if (cnt+i)%10 ==0:
            print(i)
else:
    for i in range(10):
        if (cnt+i*3)%10 ==0:
            print(i)