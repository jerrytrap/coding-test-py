import sys
from math import inf
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
dp = [inf for _ in range(k + 1)]
dp[0] = 0

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(-1 if dp[k] == inf else dp[k])
