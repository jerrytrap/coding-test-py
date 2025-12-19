import sys
input = sys.stdin.readline

a, k = map(int, input().split())
dp = [1e9 for _ in range(k + 1)]
dp[a] = 0

for i in range(a, k + 1):
    if i + 1 <= k:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    if i * 2 <= k:
        dp[i * 2] = min(dp[i * 2], dp[i] + 1)

print(dp[k])
