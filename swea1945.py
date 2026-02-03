T = int(input())
primes = (2,3,5,7,11)
for i in range(1,T+1):
    N = int(input())
    answer = [0,0,0,0,0]
    for j in  range(5):
        while N% primes[j]==0:
            answer[j]+=1
            N = N/primes[j]
    print(f'#{i}',*answer)




