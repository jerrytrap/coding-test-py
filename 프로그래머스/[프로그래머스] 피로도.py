def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n

    def dfs(k, depth):
        nonlocal answer
        answer = max(answer, depth)

        for i in range(n):
            min_k, consume_k = dungeons[i]

            if not visited[i] and k >= min_k:
                visited[i] = True
                dfs(k - consume_k, depth + 1)
                visited[i] = False

    dfs(k, 0)
    return answer
