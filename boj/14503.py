size = input().split()
size[0],size[1] = int(size[0]),int(size[1])
robot_status = input().split()
robot_status[0],robot_status[1],robot_status[2] = int (robot_status[0]),int (robot_status[1]),int (robot_status[2])

room_status = []
for i in range(size[0]):
    room_status.append(input().split())

room_status = [[int(item) for item in sublist] for sublist in room_status]
cnt = 0
#n = 0
#east = 1
#s = 2
#w =3
# print (size)
# print(robot_status)
# print(room_status)


def clean_checker (location):
    # 4칸을 돌며 0이 있는지 확인
    
    if room_status[location[0]+1][location[1]]==0 or room_status[location[0]-1][location[1]]==0 or room_status[location[0]][location[1]+1]==0 or room_status[location[0]][location[1]-1]==0 :
        return 1 # 있음 ! 반시계 북에서  서쪽(0->3 ) 서에서 남으로(3->2) 남에서 동으로(2->1) 동에서 북으로(1->0) 90도 회전 ㄱㄱ
    else:
        return 0 # 없음 후진 가능한지 확인 부탁
    
def robot_move(robot_status):
    global cnt
    if room_status[robot_status[0]][robot_status[1]] ==0:#이 자리 청소 필요하냐고 물어보기
        room_status[robot_status[0]][robot_status[1]] = 3
        cnt += 1 #청소하고 카운트 추가
    move = clean_checker([robot_status[0],robot_status[1]])#갈수 있는 곳중에 청소되는곳있냐고 물어봄
    if move == 1:## 90도 회전을 구현
        if robot_status[2] == 0:
            robot_status[2] = 3
        else : 
            robot_status[2]= robot_status[2] -1
            
        ## 움직일 칸이 청소가 필요한 칸인지 확인후 이동    
        
        if robot_status[2] ==0:
            if room_status[robot_status[0]-1][robot_status[1]] ==0:
                robot_status[0]-=1#이동
        elif robot_status[2] ==2:
            if room_status[robot_status[0]+1][robot_status[1]] ==0:
                robot_status[0]+=1#이동
        elif robot_status[2] ==1:
            if room_status[robot_status[0]][robot_status[1]+1] ==0:
                robot_status[1]+=1#이동
        elif robot_status[2] ==3:
            if room_status[robot_status[0]][robot_status[1]-1] ==0:
                robot_status[1]-=1#이동
            
            
        robot_move(robot_status)#다시 실행
    elif move ==0:
        if robot_status[2] ==0:#북쪽이면?! 남쪽으로 이동 가능 한지 물어보고
            if room_status[robot_status[0]+1][robot_status[1]] ==1: # 후진시 벽이면 그만
                return
            else : #후진 가능 하면 후진 하고 원래 부터 다시 시작
                robot_status[0] +=1
                robot_move(robot_status)
        elif robot_status[2] ==2:
            if room_status[robot_status[0]-1][robot_status[1]] ==1:
                return
            else:
                robot_status[0] -=1
                robot_move(robot_status)
        elif robot_status[2] ==1:
            if room_status[robot_status[0]][robot_status[1]-1] ==1:
                return
            else:
                robot_status[1] -=1
                robot_move(robot_status)
        elif robot_status[2] ==3:
            if room_status[robot_status[0]][robot_status[1]+1] ==1:
                return
            else:
                robot_status[1] +=1
                robot_move(robot_status)
                
robot_move(robot_status)
# print(room_status)
print(cnt)