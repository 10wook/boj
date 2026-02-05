while True:
    a = int(input())
    if a == -1:
        break

    L = []
    for i in range(1, a):
        if a % i == 0:
            L.append(i)

    if sum(L) == a:
        print(f"{a} = {' + '.join(map(str, L))}")
    else:
        print(f"{a} is NOT perfect.")
