import sys
input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
max_num = max(numbers)
dp = [[0, 0, 0, 0] for _ in range(max_num + 1)]
mod = 1_000_000_009

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, max_num + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod

for num in numbers:
    print((dp[num][1] + dp[num][2] + dp[num][3]) % mod)
