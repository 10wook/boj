N = int(input())
def numbers (number):
    if number % 2 == 0:
        return(int('8' * int(number/2)))
    elif number == 1:
        return 0
    else:
        return(int('4'+'8'*int((number-1)/2)))

answer = []
for i in range(N):
    a = int(input())
    a = numbers(a)
    answer.append(a)
for i in answer:
    print(i)