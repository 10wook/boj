import random

random.seed(42)

T = 1
N = 200
M = 50   # 파리퇴치3 기준에서 충분히 큼

with open("in_200.txt", "w") as f:
    f.write(f"{T}\n")
    f.write(f"{N} {M}\n")
    for _ in range(N):
        row = [str(random.randint(0, 30)) for _ in range(N)]
        f.write(" ".join(row) + "\n")

print("in_200.txt 생성 완료")
