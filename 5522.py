cnt = 0
while True:
    try:
        cnt += int(input())
    except EOFError:
        break
print(cnt)