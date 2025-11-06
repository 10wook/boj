import sys

def count_love(s: str):
    L = s.count('L')
    O = s.count('O')
    V = s.count('V')
    E = s.count('E')
    return L, O, V, E

yeondu = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
teams = [sys.stdin.readline().strip() for _ in range(n)]

yL, yO, yV, yE = count_love(yeondu)

def score(team: str) -> int:
    tL, tO, tV, tE = count_love(team)
    L, O, V, E = yL + tL, yO + tO, yV + tV, yE + tE
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

best = None
best_s = -1
for t in teams:
    s = score(t)
    if s > best_s or (s == best_s and (best is None or t < best)):
        best, best_s = t, s

print(best)
