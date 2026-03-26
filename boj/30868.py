T = int(input())
for _ in range(T):
    n = int(input())
    groups = n // 5
    remainder = n % 5
    result = ("++++ " * groups) + ("|" * remainder)
    print(result.rstrip())