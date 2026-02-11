for test_num in range(1,11):
    n = int(input())
    L =list(input().split("+"))
    NL =[]
    for i in L:
        if "*" in i:
            mul = 1
            A =list(map(int,i.split("*")))
            for a in A:
                mul *= int(a)
            NL.append(mul)
        else:
            NL.append(int(i))
    print(f'#{test_num} {sum(NL)}')