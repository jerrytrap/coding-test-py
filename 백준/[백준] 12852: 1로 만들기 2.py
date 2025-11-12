import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
prev = [0 for _ in range(n + 1)]
ans = []

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

x = n
while x >= 1:
    ans.append(x)
    x = prev[x]

print(dp[n])
print(' '.join(list(map(str, ans))))
