T = int(input())

def range_check(x, y):
    return 0 <= x < N and 0 <= y < N

def spray(x,y,dir)->int:
    global M,flys_matrix
    flys = [flys_matrix[x][y]]
    if dir == 1:
        for i in range(1,M):
            check = [(x+i,y),(x-i,y),(x,y+i),(x,y-i)]
            for j in check:
                if range_check(j[0],j[1]):
                    flys.append(flys_matrix[j[0]][j[1]])
                else:
                    pass
    if dir == 2:
        for i in range(1,M):
            check = [(x+i,y+i),(x-i,y-i),(x-i,y+i),(x+i,y-i)]
            for j in check:
                if range_check(j[0],j[1]):
                    flys.append(flys_matrix[j[0]][j[1]])
                else:
                    pass
        # print(flys)
    return sum(flys)
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    flys_matrix = []
    for _ in range(N):
        fly_row = list(map(int,input().split()))
        flys_matrix.append(fly_row)
    catch_case = []
    for i in range(N):
        for j in range(N):
            catch_case.append(spray(i,j,1))
            catch_case.append(spray(i,j,2))
    # print(catch_case)
    print(f'#{test_num} {max(catch_case)}')
#######################################################################

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    R = M - 1

    row = [[0]*(N+1) for _ in range(N)]
    col = [[0]*N for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            row[i][j+1] = row[i][j] + A[i][j]
            col[i+1][j] = col[i][j] + A[i][j]

    diag1_lists = [[] for _ in range(2*N-1)]
    diag1_pos = [[0]*N for _ in range(N)]

    for d in range(-(N-1), N):
        diag_id = d + (N-1)
        i0 = max(0, d)
        j0 = i0 - d
        idx = 0
        i, j = i0, j0
        while 0 <= i < N and 0 <= j < N:
            diag1_pos[i][j] = idx
            diag1_lists[diag_id].append(A[i][j])
            idx += 1
            i += 1
            j += 1

    diag1_pref = []
    for lst in diag1_lists:
        p = [0]
        for v in lst:
            p.append(p[-1] + v)
        diag1_pref.append(p)

    diag2_lists = [[] for _ in range(2*N-1)]
    diag2_pos = [[0]*N for _ in range(N)]

    for s in range(0, 2*N-1):
        i0 = max(0, s-(N-1))
        j0 = s - i0
        idx = 0
        i, j = i0, j0
        while 0 <= i < N and 0 <= j < N:
            diag2_pos[i][j] = idx
            diag2_lists[s].append(A[i][j])
            idx += 1
            i += 1
            j -= 1

    diag2_pref = []
    for lst in diag2_lists:
        p = [0]
        for v in lst:
            p.append(p[-1] + v)
        diag2_pref.append(p)

    ans = 0

    for i in range(N):
        for j in range(N):
            left = max(0, j - R)
            right = min(N-1, j + R)
            up = max(0, i - R)
            down = min(N-1, i + R)

            plus = (row[i][right+1] - row[i][left]) + (col[down+1][j] - col[up][j]) - A[i][j]

            d1 = (i - j) + (N-1)
            p1 = diag1_pos[i][j]
            lo1 = max(0, p1 - R)
            hi1 = min(len(diag1_lists[d1]) - 1, p1 + R)
            diag_sum1 = diag1_pref[d1][hi1+1] - diag1_pref[d1][lo1]

            d2 = (i + j)
            p2 = diag2_pos[i][j]
            lo2 = max(0, p2 - R)
            hi2 = min(len(diag2_lists[d2]) - 1, p2 + R)
            diag_sum2 = diag2_pref[d2][hi2+1] - diag2_pref[d2][lo2]

            xsum = diag_sum1 + diag_sum2 - A[i][j]

            ans = max(ans, plus, xsum)

    print(f"#{tc} {ans}")


