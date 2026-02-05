from collections import deque
import sys

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

# 0: 빈칸, 1: 뱀, 2: 사과
board = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r-1][c-1] = 2

L = int(input().strip())
turn_at = {}  # 시간 -> 'L' or 'D'
for _ in range(L):
    t, d = input().split()
    turn_at[int(t)] = d

# 방향: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dir = 0

snake = deque()
snake.append((0, 0))
board[0][0] = 1

time = 0
r, c = 0, 0

while True:
    time += 1
    nr, nc = r + dr[dir], c + dc[dir]

    # 벽/자기몸 충돌
    if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 1:
        print(time)
        break

    # 이동
    if board[nr][nc] == 2:
        # 사과가 있으면 길이 증가 (꼬리 유지)
        board[nr][nc] = 1
        snake.appendleft((nr, nc))
    else:
        # 사과가 없으면 머리 한 칸 전진 + 꼬리 한 칸 제거
        board[nr][nc] = 1
        snake.appendleft((nr, nc))
        tr, tc = snake.pop()
        board[tr][tc] = 0

    r, c = nr, nc

    # 회전 시각이면 방향 전환
    if time in turn_at:
        if turn_at[time] == 'D':
            dir = (dir + 1) % 4
        else:  # 'L'
            dir = (dir + 3) % 4
