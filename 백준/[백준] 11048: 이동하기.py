import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = board[0][0]
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + board[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + board[i][j]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + board[i][j]

print(dp[n - 1][m - 1])
