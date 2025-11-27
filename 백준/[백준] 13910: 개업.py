import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sizes = list(map(int, input().split()))

# 가능한 모든 요리량 생성
possible = set()

# 1개 웍 사용
for x in sizes:
    possible.add(x)

# 2개 웍 사용
for i in range(m):
    for j in range(i + 1, m):
        size = sizes[i] + sizes[j]
        if size <= n:
            possible.add(size)

dp = [1e9 for _ in range(n + 1)]
dp[0] = 0

for amount in possible:
    for i in range(amount, n + 1):
        dp[i] = min(dp[i], dp[i - amount] + 1)

print(dp[n] if dp[n] != 1e9 else -1)
