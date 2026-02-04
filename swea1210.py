T =int(input())
for test_num in range(1,T+1):
    lines = {}
    L = list(map(int,input().split()))
    line_list = []
    
    for i in range(100):
        if i ==1:
            lines[i] = []
            line_list.append(i)
    line_num = len(line_list)
    for i in  range(99):
        L = list(map(int,input().split()))
        #딕셔너리에 있는거 키 기준으로 오른쪽에 길이 있는지 없는지 보고 그 다음 숫자 
        for j in range(line_num):
            if L[line_list[j]+1] = 



    answer = 0
    print(f'#{test_num} {answer}')