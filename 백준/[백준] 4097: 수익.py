import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    p = []
    dp = [0 for _ in range(n)]

    for _ in range(n):
        p.append(int(input()))

    dp[0] = p[0]
    ans = dp[0]

    for i in range(1, n):
        dp[i] = max(p[i], dp[i - 1] + p[i])
        ans = max(ans, dp[i])

    print(ans)
