T = 10
for testcase in range(1,T+1):
    arr = []
    answer = []
    _ = int(input())
    for i in range(100):
        line = list(map(int,input().split()))
        line_sum = sum(line)
        answer.append(line_sum)
        arr.append(line)
    #여기 윈래 리스트 세로로 만들어서 sum쓰고 싶었는데 기억이 안나요
    # print("################################################",len(arr))
    for col in range(100):
        line_sum = 0
        for row in range(100):
            # print(arr[col][row],col,row)
            line_sum= line_sum + arr[row][col]
        answer.append(line_sum)
    line_sum = 0        
    for i in range(100):
        line_sum+=arr[i][i]
    answer.append(line_sum)
    line_sum = 0
    for i in range(100):
        line_sum+=arr[i][99-i]
    answer.append(line_sum)
    print(f'#{testcase} {max(answer)}')