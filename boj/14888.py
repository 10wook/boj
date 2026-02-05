N = int(input())
L = input().split()
plus, minus, mul, div = map(int,input().split())
answers = []
for i in range(len(L)):
    L[i] = int(L[i])
    
def cal (cals:list):
    answer = L[0]
    for i in range(len(cals)):
        if cals[i] == 0:  
            answer = answer + L[i+1]
        if cals[i] == 1:
            answer = answer - L[i+1]
        if cals[i] == 2:
            answer = answer * L[i+1]
        if cals[i] == 3:
            if answer > 0: 
                answer = answer // L[i+1]
            elif answer < 0:
                answer = -answer //L[i+1]
                answer = -answer
            elif answer == 0:
                answer = 0
    # print(answer) 
    return answer

# cals = []
# for i in range(plus):
#     cals.append[0]
# for i in range(minus):
#     cals.append[1]
# for i in range(mul):
#     cals.append[2]
# for i in range(div):
#     cals.append[3]
    
## 확통에서 해본 듯, 먼저 + 의 자리 수를 다 정하는 거임
## 그 다음 마이너스
## 그 다음 곱셈
## 그 다음 나눗셈
import itertools

def make_list(plus,min,mul,div):
    pos_all = range(N-1)
    answer_list = []
    for ps in itertools.combinations(pos_all,plus):
        ##덧셈 자리 추출
        #근데 여기서 남은 자리 리스트를 빼줘야 함
        mins_list = []
        for i in pos_all:
            if i in  ps:
                pass
            else:
                mins_list.append(i)
        # print(ps)
        for mins in itertools.combinations(mins_list,min):
            muls_list = []
            for j in pos_all:
                if j in  ps or j in mins:
                    pass
                else:
                    muls_list.append(j)
            for muls in itertools.combinations(muls_list,mul):
                divs_list = []
                for k in pos_all:
                    if k in  ps or k in mins or k in muls:
                        pass
                    else:
                        divs_list.append(k)
                ## 다 돌았으니까 이제 넣어서 계산 해버리자
                cal_list = []
                for i in range(N-1):
                    if i in ps:
                        cal_list.append(0)
                    if i in mins:
                        cal_list.append(1)
                    if i in muls:
                        cal_list.append(2)
                    if i in divs_list:
                        cal_list.append(3)
                # print(cal_list)
                # print(answers)
                answer_list.append(cal(cal_list))
    return answer_list

answers = make_list(plus,minus,mul,div)

print(max(answers))
print(min(answers))