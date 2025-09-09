
wheel1= list(input())
wheel2= list(input())
wheel3= list(input())
wheel4= list(input())


for i in range(8):
    wheel1[i] = int(wheel1[i] )
    wheel2[i] = int(wheel2[i] )
    wheel3[i] = int(wheel3[i] )
    wheel4[i] = int(wheel4[i] )
    
    
all_wheels = []
all_wheels.append(wheel1)
all_wheels.append(wheel2)
all_wheels.append(wheel3)
all_wheels.append(wheel4)

num = int(input())
move_list = []
for i in range(num):
    a,v = map(int,input().split())
    move_list.append([a,v])
    

def poles_check(left_wheel,right_wheel):# 극이 같은지 확인해주는 함수
    if left_wheel[2] == right_wheel[6]:
        return True
    else:
        return False
    
def trun_wheel(wheel:list,dir): #돌아간다음 어떤 상태가 되는지 알려주는 함수
    if dir == -1 :
        wheel.append(wheel[0])
        wheel.pop(0)
        return wheel
    else :
        wheel0 = wheel[-1]
        wheel.pop()
        wheel.insert(0,wheel0)
        return wheel0
    
    
def all_truns(a,d):#처음 돌아가는 방향
    
    
    plus_truns (a,a+1,d)#나랑 내 오른 쪽애 확인
    minus_turns(a,a-1,d)#나랑 내 왼쪽애
    trun_wheel(all_wheels[a-1],d)#돌아가는 애들 확인하고 돌리기
    
def plus_truns (a,b,d): # 오른쪽으로 가면서 돌아가는걸 확인하는 함수
    if a ==4 :
        return
    if poles_check(all_wheels[a-1],all_wheels[b-1]): # 여기서 트루가 나오면 안돌아감
        return
    else :#극이 다른 경우로 다음 애도 돌아가는지 확인 그리고 난 돌림
        plus_truns (b,b+1,-d)
        trun_wheel(all_wheels[b-1],-d) #오른쪽 아이를 돌린다


def minus_turns(a,b,d): #나, 내 왼쪽, 방향 이렇게 들어온다.
    if a ==1 :
        return
    if poles_check(all_wheels[b-1],all_wheels[a-1]): # 여기서 트루가 나오면 안돌아감
        return
    else :#극이 다른 경우로 다음 애도 돌아가는지 확인 그리고 난 돌림
        minus_turns (b,b-1,-d)
        trun_wheel(all_wheels[b-1],-d)
        
        
        
for i in move_list:
    all_truns( i[0],i[1])
    
cnt = 0
cnt = cnt+ all_wheels[0][0]*1
cnt = cnt+ all_wheels[1][0]*2
cnt = cnt+ all_wheels[2][0]*4
cnt = cnt+ all_wheels[3][0]*8
print(cnt)
