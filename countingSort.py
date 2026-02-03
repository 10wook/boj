def counting_sort(L:list):
    numbers= list(range(min(L),max(L)+1))
    answer = []
    #각숫자의 수를 세면서 그 수를 그 횟수만큼 추가
    for i in range(min(L),max(L)+1):
        C = L.count(i)
        for j in range(C):
            answer.append(i)

    return answer



    
    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr))  # [0, 1, 1, 1, 2, 3, 4, 4]