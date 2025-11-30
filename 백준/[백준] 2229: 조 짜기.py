import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    max_score = a[i - 1]
    min_score = a[i - 1]

    for j in range(i - 1, -1, -1):
        max_score = max(max_score, a[j])
        min_score = min(min_score, a[j])
        dp[i] = max(dp[i], dp[j] + (max_score - min_score))

print(dp[n])
