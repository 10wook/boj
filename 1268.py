N = int(input())
SL = []
for i in range(N):
    SL.append(list(map(int, input().split())))


# print(SL)
#### 원래 사고 흐름 ---
##  이걸 어떻게 저장해야 좋을까
# 1. 반 별로 인원을 저장
# 2. 번호별 학생 저장
# 3.  MAX로 뽑고 인덱스 +1 출력하면 될듯.
## 답 사고 흐름 => 여러번 같은 반은 세면 안되어서 안됨
# 같은 애들만 카운트하고 넘어감
cnt = [0] * N

for i in range(N):          # 기준 학생
    for k in range(N):      # 비교 학생
        if i == k:
            continue
        for g in range(5):  # 학년
            if SL[i][g] == SL[k][g]:
                cnt[i] += 1
                break       # 한 번이라도 같으면 끝

print(cnt.index(max(cnt)) + 1)