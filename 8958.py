N = int(input())
L = []
for i in range(N):
    L.append(input())
    
def cal_score(S:str):
    tot_cnt = 0
    cur_cnt = 1
    for i in S:
        if i == 'O':
            tot_cnt = tot_cnt + cur_cnt
            cur_cnt = cur_cnt +1
        else :
            cur_cnt = 1

    return tot_cnt


for test in L:
    print(cal_score(test))
