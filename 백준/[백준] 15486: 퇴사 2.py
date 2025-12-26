import sys
input = sys.stdin.readline

n = int(input())
time = []
profit = []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

for i in range(n - 1, -1, -1):
    end = i + time[i]

    dp[i] = max(dp[i], dp[i + 1])

    if end <= n:
        dp[i] = max(dp[i], profit[i] + dp[end])

print(dp[0])
