N = int(input())
L = []

def hanoi(start,end,temp,nums):
    #종료 조건 : 하노이 탑 1이면 종료
    # 그전까지 반복해야하는 방식
    # 짝수면 나 말고 다른 쪽으로 보내기
    global L
    # print(1)
    if nums == 1:
        L.append((start,end))
        # print(start,end)
    else:
        hanoi(start,temp,end,nums-1)
        hanoi(start,end,temp,1)
        hanoi(temp,end,start,nums-1)
hanoi(1,3,2,N)      
print(len(L))
for i in range(len(L)):
    print(L[i][0],L[i][1])
