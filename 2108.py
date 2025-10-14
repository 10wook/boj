import sys

def statistics_summary(nums):
    nums.sort()
    n = len(nums)

    # 1️⃣ 산술평균: 직접 계산 + 반올림
    avg = round(sum(nums) / n)

    # 2️⃣ 중앙값
    mid = nums[n // 2]

    # 3️⃣ 최빈값
    freq = [0] * 8001  # -4000 ~ 4000 범위
    for num in nums:
        freq[num + 4000] += 1

    max_freq = max(freq)
    mode_candidates = [i - 4000 for i, f in enumerate(freq) if f == max_freq]
    mode = mode_candidates[0] if len(mode_candidates) == 1 else mode_candidates[1]

    # 4️⃣ 범위
    range_val = nums[-1] - nums[0]

    print(avg)
    print(mid)
    print(mode)
    print(range_val)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    statistics_summary(nums)
