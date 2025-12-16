import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(h + 1)]
dp[0] = 1

for blocks in students:
    new_dp = dp[:]

    for block in blocks:
        for i in range(block, h + 1):
            new_dp[i] += dp[i - block]

    dp = new_dp

print(dp[h] % 10007)
