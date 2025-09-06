import math
room = int(input())
people_per_room = list(input().split())
for i in range (len(people_per_room)):
    people_per_room[i] = int(people_per_room[i])
    
jung,bu = input().split()
jung = int(jung)
bu = int(bu)
cnt = 0 
for i in range (room):
    if people_per_room[i] - jung <= 0:
        pass
    else :
        cnt += math.ceil((people_per_room[i] - jung) /bu)

cnt += room
print(cnt)
# print(room)
# print(people_per_room)
# print(jung,bu)