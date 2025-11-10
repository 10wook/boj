import sys

score_line = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

cnt = 0
scores = 0.0

for line in sys.stdin:
    name, time, score = line.split()
    if score == 'P':
        continue
    time = float(time)
    cnt += time
    scores += time * score_line[score]

print(scores / cnt)
