import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = p[1]

for i in range(2, n + 1):
    for j in range(i, -1, -1):
        dp[i] = max(dp[i], dp[i - j] + p[j])

print(dp[n])
