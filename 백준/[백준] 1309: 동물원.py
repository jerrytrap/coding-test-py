import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 1, 1]

for i in range(1, n):
    cur = [
        dp[0] + dp[1] + dp[2],
        dp[0] + dp[2],
        dp[0] + dp[1]
    ]

    dp = cur

print(sum(dp) % 9901)
