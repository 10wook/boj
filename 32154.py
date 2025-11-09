import sys

N = int(sys.stdin.readline())

# 등수별로 푼 문제(알파벳) 목록 — 사전순
board = [
    ["A","B","C","D","E","F","G","H","J","L","M"],         # 1등
    ["A","C","E","F","G","H","I","L","M"],                 # 2등
    ["A","C","E","F","G","H","I","L","M"],                 # 3등
    ["A","B","C","E","F","G","H","L","M"],                 # 4등
    ["A","C","E","F","G","H","L","M"],                     # 5등
    ["A","C","E","F","G","H","L","M"],                     # 6등
    ["A","C","E","F","G","H","L","M"],                     # 7등
    ["A","C","E","F","G","H","L","M"],                     # 8등
    ["A","C","E","F","G","H","L","M"],                     # 9등
    ["A","B","C","F","G","H","L","M"],                     # 10등
]

problems = board[N-1]
print(len(problems))
print(" ".join(problems))