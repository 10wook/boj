def winner(a, b):
    # a,b는 학생 번호
    if cards[a] == cards[b]:
        return min(a, b)

    if (cards[a] == 1 and cards[b] == 3) or \
       (cards[a] == 2 and cards[b] == 1) or \
       (cards[a] == 3 and cards[b] == 2):
        return a
    else:
        return b


def tournament(i, j):
    if i == j:
        return i

    mid = (i + j) // 2

    left = tournament(i, mid)
    right = tournament(mid + 1, j)

    return winner(left, right)


T = int(input())

for t in range(1, T+1):

    N = int(input())
    cards = [0] + list(map(int, input().split()))

    result = tournament(1, N)

    print(f'#{t} {result}')