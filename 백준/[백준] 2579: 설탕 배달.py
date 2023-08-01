import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [math.inf for _ in range(n + 6)]
dp[3] = 1
dp[5] = 1

for i in range(3, n + 1):
    if dp[i] != math.inf:
        dp[i+3] = min(dp[i+3], dp[i] + 1)
        dp[i+5] = min(dp[i+5], dp[i] + 1)

if dp[n] == math.inf:
    print(-1)
else:
    print(dp[n])