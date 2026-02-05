T = int(input())
for test_num in range(1,T+1):
    num = int (input())
    L = list(map(int,input().split()))
    sorted_list = sorted(L)
    print(f'#{test_num}',*sorted_list)



def bubbleSort(L:list):
    if len(L) == 1:
        return L
    else:
        length = len(L)
        for i in range(length-1):
            if L[i] > L[i+1]: #큰게 뒤로 가게 정렬
                L[i],L[i+1] = L[i+1],L[i]
        return bubbleSort(L[:-1]) + [L[-1]]

T = int(input())
for test_num in range(1,T+1):
    num = int (input())
    L = list(map(int,input().split()))
    sorted_list = bubbleSort(L)

    print(f'#{test_num}',*sorted_list)


def selection_sort(L):
    find_min = 0 #최소값 인덱스
    Length = len(L)
    for p in range(Length):
        find_min = p
        for i in range(p,Length):
            if L[i] < L[find_min]:
                find_min = i
        L[p] , L[find_min] = L[find_min],L[p]

T = int(input())
for test_num in range(1,T+1):
    num = int (input())
    L = list(map(int,input().split()))
    sorted_list = sorted(L)

    print(f'#{test_num}',*sorted_list)


    
def quick_sort(L):
    if len(L) ==1 or len(L) == 0:
        return L
    else:
        return quick_sort( [x for x in L if x < L[0]]) + [L[0]]  +quick_sort([x for x in L if x >= L[0]])


T = int(input())
for test_num in range(1,T+1):
    num = int (input())
    L = list(map(int,input().split()))
    sorted_list = sorted(L)

    print(f'#{test_num}',*sorted_list)