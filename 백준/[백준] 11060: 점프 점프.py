import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1e9 for _ in range(n)]
dp[0] = 0

for i in range(n):
    if dp[i] == 1e9:
        continue

    jump = a[i]
    for next in range(i + 1, min(n, i + jump + 1)):
        dp[next] = min(dp[next], dp[i] + 1)

print(dp[-1] if dp[-1] != 1e9 else -1)
