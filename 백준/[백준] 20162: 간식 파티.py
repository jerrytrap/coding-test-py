import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = scores[i]

    for j in range(i):
        if scores[j] < scores[i]:
            dp[i] = max(dp[i], dp[j] + scores[i])

print(max(dp))
