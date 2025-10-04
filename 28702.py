a= []
a.append(input())
a.append(input())
a.append(input())
answer = 0
for i in range(3) :
    if a[i].isdigit():
        if i==0:
            answer = int(a[i])+3
            break
        if i==1:
            answer = int(a[i])+2
            break
        if i==2:
            answer = int(a[i])+1
            break
if answer%3 == 0 and answer%5==0:
    print('FizzBuzz')
elif answer%3 == 0:
    print('Fizz')
elif answer%5 == 0:
    print('Buzz')
else:
    print(answer)