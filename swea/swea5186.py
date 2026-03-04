T = int(input())
for test_num in range(1,T+1):
    num = float(input())
    answer = ''
    temp = 0.5
    while len(answer)<13 and num != 0:
        if num >= temp:
            answer = answer+'1'
            num = num-temp
            temp = temp/2
        else :
            answer = answer+'0'
            temp = temp/2
        # print(num)
    if num == 0:
        print(f'#{test_num} {answer}')
    else:
        print(f'#{test_num} overflow')