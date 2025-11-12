def half(n: int, div: int = 10) -> int:
    if n < 10:
        return n
    r = n % div
    n -= r
    if r >= div // 2:
        n += div
    if n // div >= 10:
        return half(n, div * 10)
    return n

N = int(input())
print(half(N))