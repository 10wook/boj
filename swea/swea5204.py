
def merge_sort(arr):
    global cnt
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    if left[-1] > right[-1]:
        cnt += 1
        
    result = []
    l = r = 0
    
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            
    result += left[l:]
    result += right[r:]
    
    return result


T = int(input())

for t in range(1, T+1):
    
    N = int(input())
    arr = list(map(int,input().split()))
    
    cnt = 0
    
    arr = merge_sort(arr)
    
    print(f'#{t} {arr[N//2]} {cnt}')