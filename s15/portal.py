T = int(input())
for test_num in range(1,T+1):
    roomnum = int(input()) #방 번호 마지막
    rooms = list(map(int,input().split()))
    #방 별 포탈 2개
    # 젤먼저 들어오면 걍 바로 오른쪽으로 감
    # 짝수번째로 들어오면 왼쪽 어딘가로 가는 포탈을 탐
    # 단 1번방 (2번째 인덱스의 방은 걍 무조건 다음 방으로감 감)
    roomstats = [0]*roomnum
    # print(roomstats)
    curr = 0
    moves = 0
    while curr != roomnum-1:
    # for _ in range(12):
        # print(f'방문한 방은 {curr} 이며 방상태는 {roomstats[curr]}',end = '')
        if curr == 0:
            roomstats[curr] =1
            curr+=1
            moves+=1 
            
        elif roomstats[curr] == 0: #맨 처음에 들어왔고 바로 왼쪽으로 가는 포탈을 타야함
            roomstats[curr] = 1
            curr = rooms[curr]-1 # 이 방의 포탈이 나를 이끄는 곳으로 가야한다
            moves+=1
            #그리고 룸 상태를 방문 상태로 바꾼다
            
           
        else: # 두번재 들어왔을떄 부터는 걍 오른쪽으로 쭉 간다.
            curr += 1
            moves+=1
        
        # print(f'이제 방 {curr}로 갑니다.')



    print(f'#{test_num} {moves}')
