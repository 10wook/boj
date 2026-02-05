T = int(input())

for test_num in range(1, T + 1):
    lines = {}
    line_list = []

    # 첫 줄: 세로선 수집
    first = list(map(int, input().split()))
    for c in range(100):
        if first[c] == 1:
            lines[c] = set()
            line_list.append(c)

    line_num = len(line_list)

    # 중간 98줄: 가로선 저장
    for r in range(1, 99):
        L = list(map(int, input().split()))
        for i in range(line_num - 1):
            c1 = line_list[i]
            c2 = line_list[i + 1]
            if L[c1] == 1 and L[c2] == 1:
                lines[c1].add((r, c2))
                lines[c2].add((r, c1))

    # 마지막 줄
    last = list(map(int, input().split()))
    col = last.index(2)
    row = 99

    # 🔥 핵심: row + col 상태 유지
    while row > 0:
        moved = False
        for h, nxt in lines.get(col, []):
            if h == row:
                col = nxt        # 같은 행에서 좌/우 이동
                moved = True
                break
        if not moved:
            row -= 1            # 좌우 없을 때만 위로

    print(f'#{test_num} {col}')



