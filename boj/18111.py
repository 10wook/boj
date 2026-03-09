import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]

# 각 높이에 대한 블록 수를 계산
height_count = {}
for i in range(N):
    for j in range(M):
        height = world[i][j]
        if height in height_count:
            height_count[height] += 1
        else:
            height_count[height] = 1

# 최소 높이와 최대 높이 구하기
min_height = min(height_count.keys())
max_height = max(height_count.keys())

answer = float('inf')
height = 0

# 최소 높이부터 최대 높이까지 각 높이에 대해 계산
for h in range(min_height, max_height + 1):
    add = 0
    temp_B = B
    
    # 각 높이에 대한 블록 추가 및 제거 계산
    for current_height, count in height_count.items():
        if current_height > h:
            # 블록을 제거해야 하는 경우
            add += 2 * (current_height - h) * count
            temp_B += (current_height - h) * count
        elif current_height < h:
            # 블록을 추가해야 하는 경우
            add += (h - current_height) * count
            temp_B -= (h - current_height) * count
    
    # 블록이 부족하면 넘어가기
    if temp_B < 0:
        continue
    
    # 더 적은 비용이 나오면 갱신
    if add <= answer:
        answer = add
        height = h

print(answer, height)