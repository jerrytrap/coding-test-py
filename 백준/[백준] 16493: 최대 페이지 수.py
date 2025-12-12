import sys
input = sys.stdin.readline

n, m = map(int, input().split())
info = []
dp = [0 for _ in range(n + 1)]

for _ in range(m):
    info.append(tuple(map(int, input().split())))

for day, page in info:
    for i in range(n, -1, -1):
        if i - day >= 0:
            dp[i] = max(dp[i], dp[i - day] + page)

print(dp[n])
