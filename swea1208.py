
def dump(L:list) -> list:
    L[-1]= L[-1]-1
    L[0] = L[0]+1
    return L

for i in range(1,11):
    dumps = int(input())
    ground = list(map(int,input().split()))
    # print(ground)
    #조건이 만족될때까지 반복
    while True:
        ground = sorted(ground)
        if ground[-1] - ground[0] == 1 or ground[-1] - ground[0] == 0:
            break 
        dump(ground)
        dumps -=1   
        if dumps ==0:
            break

    answer = max(ground)-min(ground)
    print(f'#{i} {answer}')
