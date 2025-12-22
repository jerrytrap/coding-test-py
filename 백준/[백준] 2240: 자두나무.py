import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w + 1)] for _ in range(t)]

# 0초에 1번 자두나무 아래에 위치한 경우
dp[0][0] = 1 if tree[0] == 1 else 0
# 0초에 2번 자두나무 아래에 위치한 경우
# 자두는 처음에 1번 자두나무 아래에 있으므로 1번 이동해야함
dp[0][1] = 1 if tree[0] == 2 else 0

for i in range(1, t):
    for j in range(w + 1):
        pos = 1 if j % 2 == 0 else 2

        # 이동하지 않는 경우
        best = dp[i - 1][j]

        # 이동하는 경우
        if j > 0:
            best = max(best, dp[i - 1][j - 1])

        # 이동한 위치에 자두가 떨어지는 경우 +1
        if tree[i] == pos:
            best += 1

        dp[i][j] = best

print(max(dp[t - 1]))
