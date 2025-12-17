import sys
input = sys.stdin.readline

n = int(input())
small_jump = [0 for _ in range(n)]
big_jump = [0 for _ in range(n)]

for i in range(n - 1):
    s, b = map(int, input().split())
    small_jump[i] = s
    big_jump[i] = b

k = int(input())
dp = [[1e9, 1e9] for _ in range(n)]
dp[0][0] = 0

for i in range(n):
    for j in range(2):
        if dp[i][j] == 1e9:
            continue

        if i + 1 < n:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + small_jump[i])

        if i + 2 < n:
            dp[i + 2][j] = min(dp[i + 2][j], dp[i][j] + big_jump[i])

        if j == 0 and i + 3 < n:
            dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)

print(min(dp[n - 1][0], dp[n - 1][1]))
