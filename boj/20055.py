N, K = map(int,input().split())
A = input().split()
RSL = [] #로봇 상태 리스트 (로봇의 위치와 번호 저장기)
for i in range(2*N):
    A[i] = int(A[i])
    RSL.append(0) 
def stop_check(A:list,K): # 만약 멈추는 조건이라면 트루 계속하는 조건이라면 false
    cnt = 0
    for i in A:
        if i <= 0:
            cnt+=1
    if K <= cnt:
        return True
    else:
        return False
    
def step_1(A:list,RSL:list): #로봇의 위치 교체하기(벨트 한칸 밀기)
    A2 = []
    RSL2 =[]
    A2.append(A[-1])
    RSL2.append(RSL[-1])
    for i in range((2*N)-1):
        A2.append(A[i])
        RSL2.append(RSL[i])
    A = A2
    RSL = RSL2
    RSL[N-1] = 0
    return A,RSL
    
    
    
##로봇 올리기 스텝

def step_3(A:list,RSL:list,turn_cnt):## 벨트 내구도,로봇 상태, 차례 카운트 0자리에 로봇 올리고, 내구도 깎고
    if A[0] != 0:
        RSL[0] = turn_cnt
        A[0] -=1

def step_2(A:list,RSL:list):#제일 턴수가 작은애 부터 돌면서 올리면 되는데, 아마 제일 오른쪽에 있는 애부터 돈다고 생각하면 될듯
    for i in range(N-2,-1,-1): #내리는 칸 전부터 올리는 칸 까지 확인
        if RSL[i+1] == 0 and RSL[i] != 0 and A[i+1] >= 1: #내구도 1이상 & 로봇 그 자리에 없음 & 원래 자리에 로봇 있음
            RSL[i+1] = RSL[i]#로봇 옮기고 
            RSL[i] = 0 #원래 자리 비우고
            A[i+1] -=1 #옮겨간 곳 내구도 깎고
    RSL[N-1] = 0 # 만약에 내리는 자리 가면 또 없애고
    
    
turn_cnt = 0
while True:
    turn_cnt +=1
    # print("시작상태",turn_cnt,A)
    # print("시작 상태",turn_cnt,RSL)
    A,RSL = step_1(A,RSL)
    # print("단계",turn_cnt,'조건1',A)
    # print("단계",turn_cnt,'조건1',RSL)
    step_2(A,RSL)
    # print("단계",turn_cnt,'조건2',A)
    # print("단계",turn_cnt,'조건2',RSL)
    step_3(A,RSL,turn_cnt)
    # print("단계",turn_cnt,'조건3',A)
    # print("단계",turn_cnt,'조건3',RSL)
    # print("스텝",turn_cnt,A)
    # print("스템",turn_cnt,RSL)
    if stop_check(A,K):
        break
    # print(turn_cnt)
print(turn_cnt)