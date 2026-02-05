T = int(input())

def check(i1,i2):
    answer = str(i1*i2)
    temp = '0'
    for i in answer:
        if i >= temp:
            temp = i
        else:
            return False
    return True
for test_num in range(1,T+1):
    num = int(input())
    L = list(map(int,input().split()))
    answer = []
    for i in range(num):
        for j in range(i+1,num):
            if check(L[i],L[j]):
                answer.append(L[i]*L[j])
    if answer:
        print(f'#{test_num}',max(answer))
    else:
        print(f'#{test_num}',-1)
    
    
