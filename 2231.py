N = int(input())
answer = 0
for i in range(N):
    L =[]
    temp_N = i    
    while True:
        if temp_N//10 == 0:
            L.append(temp_N)
            break
        else:
            L.append(temp_N%10)
            temp_N = temp_N//10
    checker = 0
    # print(L)
    for j in L:
        checker+=j
    checker += i
    if checker ==N:
        answer = i
        break
    
print(answer)