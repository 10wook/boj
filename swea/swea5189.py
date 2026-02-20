T = int(input())
from itertools import permutations
for test_num in range(1,T+1):
    answer = float('inf')
    N = int(input())
    L = [list(map(int,input().split())) for _ in range(N)]

    for i in permutations(range(1,N),N-1):
        temp = 0
        temp+=L[0][i[0]]
        for j in range(1,len(i)):
            temp+=L[i[j-1]][i[j]]
        temp+=L[i[-1]][0]
        answer = min (answer,temp)
    print(f'#{test_num} {answer}')