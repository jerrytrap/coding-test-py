import sys
input = sys.stdin.readline

n, k = map(int, input().split())
caffeines = list(map(int, input().split()))
dp = [1e9 for _ in range(k + 1)]
dp[0] = 0

for c in caffeines:
    for i in range(k, c - 1, -1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[k] if dp[k] != 1e9 else -1)
