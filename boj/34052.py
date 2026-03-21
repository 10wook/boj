times = [int(input()) for _ in range(4)]

if sum(times) + 300 <= 1800:
    print("Yes")
else:
    print("No")