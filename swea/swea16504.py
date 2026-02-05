T = int(input())
for test_num in range(1,T+1):
    num = int (input())
    L = list(map(int,input().split()))
    #L을 돌면서  본인 인덱스 - 내 뒤에 작은 애들의 수를 뺀 값중 제일 큰거 출력
    answer_list = []
    for towers in range(num):
        cnt = 0
        for i in range(towers+1,num):
            if L[towers] > L[i]:
                cnt +=1
        answer_list.append(cnt)


    print(f'#{test_num} {max(answer_list)}')