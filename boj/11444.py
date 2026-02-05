N = int(input())
MOD = 1000000007

def fib_fast_iter(n):
    # 상태: (a, b) = (F(m), F(m+1)), 처음엔 m=0 => (0,1)
    a, b = 0, 1
    # n의 최상위 비트부터 내려가며 처리
    for bit in bin(n)[2:]:
        # doubling: m -> 2m
        c = (a * ((2*b - a) % MOD)) % MOD      # F(2m)
        d = (a*a + b*b) % MOD                  # F(2m+1)
        a, b = c, d
        # 만약 현재 비트가 1이면 한 스텝 더: 2m -> 2m+1
        if bit == '1':
            a, b = b, (a + b) % MOD
    return a  # = F(n)

print(fib_fast_iter(N) % MOD)
