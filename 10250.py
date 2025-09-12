N = int(input())
for i in range(N):
    floor,room,guest = map(int,input().split())
    # print(floor,room,guest)
    room_num1 = guest//floor
    room_num = guest//floor+1

    if room_num>=10:
        room_num=str(room_num)
    else:
        room_num='0'+str(room_num)
    # print(guest%floor)#나머지 나누기
    # print(guest//floor) # 몫 나누기
    if guest%floor ==0:
        if room_num1>=10:
            room_num1=str(room_num1)
        else:
            room_num1='0'+str(room_num1)
        
        print(str(floor)+str(room_num1))
    else:
        print(str(guest%floor)+room_num)