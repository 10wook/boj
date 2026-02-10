def dfs(start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            #지금 방문을 한거고
            # 방문한 지금 이순간!
            #하고 싶었던 일들을 여기서 수행하시면 됩니다.
            for next in reversed(graph[v]):
                stack.append(next)