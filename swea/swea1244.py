def dfs(cnt):
    if cnt == K:
        # K번째 교환에 도달했을 때만 결과 세트에 추가
        results.add("".join(nums))
        return

    for i in range(N):
        for j in range(i + 1, N):
            nums[i], nums[j] = nums[j], nums[i]
            
            state = ("".join(nums), cnt)
            if state not in visited:
                visited.add(state)
                dfs(cnt + 1)
            
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())

for tc in range(1, T + 1):
    num, K = input().split()
    nums = list(num)
    K = int(K)
    N = len(nums)

    results = set()  # K번째 결과들을 저장할 세트
    visited = set()  # 중복 탐색 방지용

    dfs(0)

    ans = max(int(x) for x in results)  # results에서 최댓값 찾기
    print(f"#{tc} {ans}")