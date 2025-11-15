import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # A를 입력하는 경우
    dp[i] = dp[i - 1] + 1

    # j번 입력된 A를 복붙하는 경우
    for j in range(1, i - 2):
        dp[i] = max(dp[i], dp[j] * (i - j - 1))

print(dp[n])
