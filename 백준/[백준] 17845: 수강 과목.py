import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lectures = [tuple(map(int, input().split())) for _ in range(k)]
dp = [0 for _ in range(n + 1)]

for i, t in lectures:
    for time in range(n, t - 1, -1):
        dp[time] = max(dp[time], dp[time - t] + i)

print(dp[n])
