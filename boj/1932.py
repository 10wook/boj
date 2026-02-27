N = int(input())
tri = []

tri = [list(map(int,input().split())) for _ in range(N)]
#print(tri)
# 이 자리까지 오는 최댓값을 저장해 두면 될것 같긴해.
largest_list = []
for stage in tri:
    if len(stage) ==1:
        largest_list.append([0])
    largest_list.append([])
    for i in range(0,len(stage)):
        if i ==0 :
            largest_list[-1].append(largest_list[-2][0]+stage[0])
        elif i == (len(stage)-1):
            largest_list[-1].append(largest_list[-2][-1]+stage[-1])
        else:
            largest_list[-1].append(max(largest_list[-2][i-1],largest_list[-2][i])+stage[i])
# print(largest_list)
print(max(largest_list[-1]))