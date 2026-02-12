w,h = map(int,input().split())
x,y = map(int,input().split())
time = int(input())
dx = 1
dy = 1
# 시간 초과 코드
# for i in range(time):
#     if x == w:
#         dx = -1
#     if y == h :
#         dy = -1
#     if x == 0:
#         dx = 1
#     if y == 0:
#         dy = 1
#     x += dx
#     y += dy




# X 다 더하고 Y다 더하고
# 각각 x,y로 나누고 방향 정하고 마지막에 출발해주면될듯/ 짝수면 증가중 홀수면 감소중인듯
if ((x + time)//w) %2 == 0:
    x = 0 + (x + time)%w
else:
     x = w - (x + time)%w
if ((y + time)//h) %2 == 0:
    y  = 0 + (y+ time)%h
else:
     y = h - (y + time)%h
print(x, y)