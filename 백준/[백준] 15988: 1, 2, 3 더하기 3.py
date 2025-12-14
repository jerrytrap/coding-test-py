import sys
input = sys.stdin.readline

t = int(input())
cases = [int(input()) for _ in range(t)]
max_case = max(cases)
dp = [0 for _ in range(max_case + 3)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_case + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for case in cases:
    print(dp[case])
