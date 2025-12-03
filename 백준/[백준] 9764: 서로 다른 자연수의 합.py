import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(2001)]
dp[0] = 1

for i in range(1, 2001):
    for j in range(2000, i - 1, -1):
        dp[j] += dp[j - i]

for _ in range(t):
    n = int(input())
    print(dp[n] % 100999)
