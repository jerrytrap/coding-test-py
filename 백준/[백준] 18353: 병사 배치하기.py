import sys
input = sys.stdin.readline

n = int(input())
soliders = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if soliders[j] > soliders[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
