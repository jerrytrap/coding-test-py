import sys
input = sys.stdin.readline

dp = [0 for _ in range(10001)]
dp[0] = 1

for i in (1, 2, 3):
    for j in range(i, 10001):
        dp[j] += dp[j - i]

t = int(input())
for _ in range(t):
    num = int(input())
    print(dp[num])
