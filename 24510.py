C = int(input())
answer = 0

for _ in range(C):
    line = input().strip()
    cnt = line.count("for") + line.count("while")
    answer = max(answer, cnt)

print(answer)
