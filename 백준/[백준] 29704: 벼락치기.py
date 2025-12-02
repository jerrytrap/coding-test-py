import sys
input = sys.stdin.readline

n, t = map(int, input().split())
problems = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(t + 1)]

total_penalty = sum(m for d, m in problems)

for day, money in problems:
    for time in range(t, day - 1, -1):
        dp[time] = max(dp[time], dp[time - day] + money)

answer = total_penalty - dp[t]
print(answer)
