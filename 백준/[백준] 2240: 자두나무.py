import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w + 1)] for _ in range(t)]

for i in range(w + 1):
    pos = 1 if i % 2 == 0 else 2
    dp[0][i] = 1 if tree[0] == pos else 0

for i in range(1, t):
    for j in range(w + 1):
        pos = 1 if j % 2 == 0 else 2

        best = dp[i - 1][j]

        if j > 0:
            best = max(best, dp[i - 1][j - 1])

        if tree[i] == pos:
            best += 1

        dp[i][j] = best

print(max(dp[t - 1]))
