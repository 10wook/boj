N,M = map(int,input().split())
water_stat = []
cloud_stat = []
for i in range(N):
    water_stat.append(input().split())
    
for i in range(N):
    cloud_stat.append([])
    for j in range(N):
        water_stat[i][j] = int(water_stat[i][j])
        cloud_stat[i].append(0)


    
    
    
    
def water_counter(water_stat):
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += water_stat[i][j] 
    return cnt 


def make_rain(cloud_stat):   
    cloud_stat[N-1][0] = 1
    cloud_stat[N-1][1] = 1
    cloud_stat[N-2][0] = 1
    cloud_stat[N-2][1] = 1
    
def move_cloud(cloud_stat,dir,distance):
    distance = distance%N
    if dir == 1 :
        cloud_stat = move_cloud_left(cloud_stat,distance)
    if dir == 2 :
        cloud_stat = move_cloud_left(cloud_stat,distance)
        cloud_stat = move_cloud_up(cloud_stat,distance)
    if dir == 3 :
        cloud_stat = move_cloud_up(cloud_stat,distance)
    if dir == 4 :
        cloud_stat = move_cloud_up(cloud_stat,distance)
        cloud_stat = move_cloud_right(cloud_stat,distance)
    if dir == 5 :
        cloud_stat = move_cloud_right(cloud_stat,distance)
    if dir == 6 :
        cloud_stat = move_cloud_right(cloud_stat,distance)
        cloud_stat = move_cloud_down(cloud_stat,distance)
    if dir == 7 :
        cloud_stat = move_cloud_down(cloud_stat,distance)
    if dir == 8 :
        cloud_stat = move_cloud_down(cloud_stat,distance)
        cloud_stat = move_cloud_left(cloud_stat,distance)
        
    return cloud_stat
        
        
    



def move_cloud_left(cloud_stat,distance):#이미 나머지만 들어온 상태
    #움직인거리를 N으로 나누고, 나머지 만큼 움직인다. j를 기준으로 나머지 원래 값 - 거리
    #양수면 그대로 두고
    #음수면 N을 추가해준 값을 돌려주면 되겠다.
    new_cloud_stat = []
    for i in range(N):
        new_cloud_stat.append([])
        for j in range(N):
            new_cloud_stat[i].append(0)
            
    for i in range(N):
        for j in range(N):
            if j -distance >= 0:
                new_cloud_stat[i][j-distance] = cloud_stat[i][j]
            else:
                new_cloud_stat[i][j-distance+N] = cloud_stat[i][j]

    return new_cloud_stat
                
def move_cloud_up(cloud_stat,distance):#이미 나머지만 들어온 상태
    #움직인거리를 N으로 나누고, 나머지 만큼 움직인다. j를 기준으로 나머지 원래 값 - 거리
    #양수면 그대로 두고
    #음수면 N을 추가해준 값을 돌려주면 되겠다.
    new_cloud_stat = []
    for i in range(N):
        new_cloud_stat.append([])
        for j in range(N):
            new_cloud_stat[i].append(0)
            
    for i in range(N):
        for j in range(N):
            if i -distance >= 0:
                new_cloud_stat[i-distance][j] = cloud_stat[i][j]
            else:
                new_cloud_stat[i-distance+N][j] = cloud_stat[i][j]
    return new_cloud_stat


def move_cloud_right(cloud_stat,distance):#이미 나머지만 들어온 상태
    #움직인거리를 N으로 나누고, 나머지 만큼 움직인다. j를 기준으로 나머지 원래 값 - 거리
    #양수면 그대로 두고
    #음수면 N을 추가해준 값을 돌려주면 되겠다.
    new_cloud_stat = []
    for i in range(N):
        new_cloud_stat.append([])
        for j in range(N):
            new_cloud_stat[i].append(0)
            
    for i in range(N):
        for j in range(N):
            if j + distance > (N-1):
                new_cloud_stat[i][j+distance-N] = cloud_stat[i][j]
            else:
                new_cloud_stat[i][j+distance] = cloud_stat[i][j]

    return new_cloud_stat
                
def move_cloud_down(cloud_stat,distance):#이미 나머지만 들어온 상태
    #움직인거리를 N으로 나누고, 나머지 만큼 움직인다. j를 기준으로 나머지 원래 값 - 거리
    #양수면 그대로 두고
    #음수면 N을 추가해준 값을 돌려주면 되겠다.
    new_cloud_stat = []
    for i in range(N):
        new_cloud_stat.append([])
        for j in range(N):
            new_cloud_stat[i].append(0)
            
    for i in range(N):
        for j in range(N):
            if i + distance > (N-1):
                new_cloud_stat[i+distance-N][j] = cloud_stat[i][j]
            else:
                new_cloud_stat[i+distance][j] = cloud_stat[i][j]
    return new_cloud_stat


def water_increase (water_stat,cloud_stat):
    increased_loc = []
    for i in range(N):
        for j in range(N):
            if cloud_stat[i][j] == 1 :
                water_stat[i][j] += 1 #비가 와서 물이 증가함
                cloud_stat[i][j] = 2 #구름이 막 없어진걸 표현하는 칸
                increased_loc.append([i,j])
    return increased_loc

def water_copy_bug(water_stat,incresed_loc):
    #늘어난 위치를 돌면서 4방 대각선에 대해서 범위를 안 넘으면 물을 추가한다
    for i in incresed_loc:
        #왼쪽 위
        if i[0] - 1 >= 0 and i[1] - 1 >= 0 and water_stat[i[0] - 1][i[1] - 1] > 0:
            water_stat[i[0]][i[1]] +=1
        #오른쪽 위
        if i[0] - 1 >= 0 and i[1] + 1 <= (N-1) and  water_stat[i[0] - 1][i[1] + 1] > 0:
            water_stat[i[0]][i[1]] +=1
        #오른쪽 아래
        if i[0] + 1 <= (N-1) and i[1] + 1 <= (N-1) and water_stat[i[0] + 1][i[1] + 1] > 0:
            water_stat[i[0]][i[1]] +=1
        #왼쪽 아래
        if i[0] + 1 <= (N-1) and i[1] - 1 >= 0 and water_stat[i[0] + 1][i[1] - 1] > 0:
            water_stat[i[0]][i[1]] +=1
    return water_stat


def natural_cloud(water_stat,cloud_stat):
    for i in range(N):
        for j in range(N):
            if water_stat[i][j] >= 2 and cloud_stat[i][j] != 2:
                #만약 물이 많고 방금 비가 온 곳 아니라면??
                water_stat[i][j] -= 2
                cloud_stat[i][j] = 1
            if cloud_stat[i][j] == 2:
                cloud_stat[i][j] = 0
                
                
make_rain(cloud_stat)                
for i in range(M):
    dir , distance = map(int,input().split())
    cloud_stat = move_cloud(cloud_stat,dir,distance)
    increased_loc = water_increase(water_stat,cloud_stat)
    water_copy_bug(water_stat,increased_loc)
    natural_cloud(water_stat,cloud_stat)
    # print('===================')
    # for i in range(N):
    #     print(water_stat[i])
    # print('===================')
print(water_counter(water_stat))