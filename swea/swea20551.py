T = int(input())
for test_num in range(1,T+1):
    candys = list(map(int,input().split()))
    answer = 0
    if candys[-1] <= candys[1]:
        #만약 앞 숫자가 크다면 작아지게 만든다.
        diff = candys[1]- (candys[-1]-1)
        answer += diff
        candys[1] -= diff
    if candys[1] <= candys[0]:
        diff = candys[0] - (candys[1]-1)
        answer += diff
        candys[0] -= diff
    # print(candys,answer)
    if candys[0] <= 0 or candys[1]<=0 or candys[2] <=0:
        answer = -1
    print(f'#{test_num} {answer}')