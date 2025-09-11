N = int(input())
students = []
for i in range (N*N):
    students.append(input().split())
    
##이렇게 하면 일단 그냥 다 문자열로 저장만 된 상태
students_love_dict = dict()
for i in range (N*N):
    for j in range(len(students[i])):
        students[i][j] = int(students[i][j])
        
for i in range (N*N):
    students_love_dict[students[i][0]] = students[i][1:]
students_love_dict[0] = [0,-1,-2,-3,-4]
## 딕셔너리에 전부 저장 완료
##가깝다는 걸 확인하는 법
### 지금 필요한건 반의 자리 배치가 어떻게 되어있는지 확인해야함  
seat_list = []
for i in range(N):
    seat_list.append([])
    for j in range(N):
        seat_list[i].append(0)
        
###### 보드도 만들었으니까 이제 기본 설정 진짜 끝
#0은 비어있는 칸, 양수 숫자는 학생이 앉은 자리, 음수는 단계 처리 자리 일단 0단계부터 처리하는 법을 배워보도록해용

def return_nexted_seat(seat:list):#자리 하나를 입력 받으면 [n,m]형태, 인접한 자리의 좌표를 출력한다.
    nexted_seat = []
    if seat[0] < N-1:
        nexted_seat.append([seat[0]+1,seat[1]])
    if seat[0] > 0 :
        nexted_seat.append([seat[0]-1,seat[1]])
    if seat[1] < N-1:
        nexted_seat.append([seat[0],seat[1]+1])
    if seat[1] > 0 :
        nexted_seat.append([seat[0],seat[1]-1])
    return nexted_seat

def love_friend_check(student_num,nexted_seat):## 해당 자리에 인접한 곳에 좋아하는 학생이 몇명이나 있는지 확인할 것
    global seat_list
    cnt = 0
    for i in nexted_seat:
        if seat_list[i[0]][i[1]] in students_love_dict[student_num] :
            cnt+=1
    # if student_num ==0 :
        # print(cnt)
    return cnt


def count_people(seat_list):## 계산해봤을때 다음 단계에 평가해봐야하는 좌표를 출력해준다 
    #돌면서 좌표값이 제일 낮은 애들을 출력해주었다~~
    # 0 이 들어와서 들어간 애들은  0~-4까지 비교하고 제일 낮은 애들을 좌표값 반환해준다
    return_list = []
    lowest_num = 0
    for i in range (N):
        for j in range(N):
            # print(seat_list[i][j])
            if seat_list[i][j] < lowest_num:
                lowest_num = seat_list[i][j]
                return_list = []
                return_list.append([i,j])
            elif seat_list[i][j] == lowest_num:
                return_list.append([i,j]) 
            else:
                pass
    return return_list ## 이제 여기를 기반으로 다음 스텝을 넘겨서 확인해 보아요

def clear_seat_list(seat_list):
    for i in range(N):
        for j in range(N):
            if seat_list[i][j] < 0:
                seat_list[i][j] = 0
    return seat_list



def step_1(student_num): #모든 빈자리를 돌면서 인접한 학생이 제일 많은 자리를 찾는다.
    global seat_list
    
    for seat_line in range (N):
        for seat in range(N):
            if seat_list[seat_line][seat] ==0 :
                next_seats = return_nexted_seat([seat_line,seat])
                seat_list[seat_line][seat] =  - love_friend_check(student_num,next_seats) # 인접한 좋아하는 애가 음수의 형태로 입력 된다
                ## 가장 인접한 아이가 많은 자리 좌표의 리스트를 뽑는다.
    # print(seat_list)
    next_step_check_need = count_people(seat_list)
    if len(next_step_check_need) ==1:
        seat_list[next_step_check_need[0][0]][next_step_check_need[0][1]] = student_num
        seat_list = clear_seat_list(seat_list)
    else :
        seat_list = clear_seat_list(seat_list)
        step_2(next_step_check_need,student_num)


# def step_2(need_step2_check,student_num):
#     global seat_list
#     # 입력 받은 좌표만 돌면서 빈자리가 몇개있는지 세어 볼 것
#     # print(need_step2_check)
#     for i in need_step2_check:
#         next_seats = return_nexted_seat([i[0],i[1]])
#         a = - love_friend_check(0,next_seats)
#         # print(a)
#         seat_list[i[0]][i[1]] =  a## 좌표가 0인거 세어서 좀 넣어줘잉
#     next_step_check_need = count_people(seat_list)
#     # print(next_step_check_need)
#     seat_list = clear_seat_list(seat_list)
#     seat_list[next_step_check_need[0][0]][next_step_check_need[0][1]] = student_num
    
def step_2(need_step2_check, student_num):
    global seat_list
    # 후보 칸마다 '인접한 빈칸 수'를 세어 음수로 기록(0개여도 -1이 되게)
    for x, y in need_step2_check:
        next_seats = return_nexted_seat([x, y])

        # 빈칸 세기: 0(완전 빈칸) + 이전에 표기한 음수(임시)도 빈칸 취급
        empty_cnt = 0
        for nx, ny in next_seats:
            if seat_list[nx][ny] <= 0:
                empty_cnt += 1

        seat_list[x][y] = -(empty_cnt + 1)  # ★ 핵심 수정: 항상 음수로

    # 가장 작은(=가장 음수) 값들만 추려오면 step2 타이브레이크(빈칸 많은 것) 충족
    next_step_check_need = count_people(seat_list)

    # 행/열 작은 것 우선은 count_people의 순회(행→열)로 자동 충족
    seat_list = clear_seat_list(seat_list)
    seat_list[next_step_check_need[0][0]][next_step_check_need[0][1]] = student_num

    
    
def count_score (seat_list) :
    score_cnt = 0
    for i in range (N):
        for j in range (N):
            next_seats = return_nexted_seat([i,j])
            cnt = love_friend_check(seat_list[i][j],next_seats)
            if cnt == 0 :
                pass
            elif cnt ==1:
                score_cnt += 1
            elif cnt ==2:
                score_cnt += 10
            elif cnt ==3:
                score_cnt += 100
            elif cnt ==4:
                score_cnt += 1000
                
    return score_cnt


for i in students:
    step_1(i[0])

print(count_score (seat_list))
# for i in range (N):
#     print(seat_list[i])