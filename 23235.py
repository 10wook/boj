# The Fastest Sorting Algorithm In The World
case = 1
while True:
    try:
        nums = list(map(int, input().split()))
        if nums[0] == 0:  # 0이면 입력 종료
            break
        print(f"Case {case}: Sorting... done!")
        case += 1
    except EOFError:
        break
