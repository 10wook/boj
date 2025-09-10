import itertools
N,M = map(int,input().split())
L = []
for i in range(N):
    L.append(list(input().split()))
H_list = []
C_list = []
for i in range (N):
    for j in range(N):
        if L[i][j] == '1':
            H_list.append([i,j])
        elif L[i][j] == '2':
            C_list.append([i,j])
#######################################
#입력 받기 끝
# 맨허튼 거리 계산기
#
def cal_chicken_distance(H:list,C:list):#리스트 형태로 [r,c]를 두개 입력 받으면 될듯
    return max((H[0] - C[0]),-(H[0] - C[0]))+max((H[1] - C[1]),-(H[1] - C[1]))## 각각 절댓값 계산 후 더해서 출력

#M개 고르는 조합을 구해서 쭉 입력해주고, 최솟값을 또 계산해서 갖고 있어야 겠네
#집 하나랑 치킨집리스트 전체 넣어주고 젤 가까운 곳이 어딘지 확인 할 것
def cal_nearest_chicken(H:list,C_L:list):
    distance = float('inf')
    for i in C_L:
        # print(cal_chicken_distance(H,i))
        distance  = min(distance,cal_chicken_distance(H,i))
    # print("house-chi",distance)
    return distance

## 모든 집에 대해서 제일 짧은 거리 구해서 다 더한 값을 출력할 것
def cal_all_distance(H_L:list,C_L:list):
    cnt = 0
    for i in H_L:
        # print(cal_nearest_chicken(i,C_L))
        cnt = cnt + cal_nearest_chicken(i,C_L)
    return cnt## 이 경우에 계산된 최저 거리 출력


def cal_shortest_CD(H_L:list,C_L:list):
    cnt = float('inf')
    for Cs in itertools.combinations(range(len(C_L)),M):#조합을 계산해둠 
        CL = []
        #계산된 조합 애들을 여기에 넣어준다 
        # Cs에 튜플 형태로 00번째 치킨집이 들어있음
        for i in Cs:#C_L에서 추출 해서 CL에 넣고 작은 값 계산하기
            CL.append(C_L[i])
            
        # print(cal_all_distance(H_L,CL))
        cnt = min(cal_all_distance(H_L,CL),cnt)
    
    return cnt
    
print(cal_shortest_CD(H_list,C_list))