import sys
input = sys.stdin.readline

n = int(input())
max_late = 2
max_absent = 3
mod = 1000000
dp = [[[0 for _ in range(max_absent)] for _ in range(max_late)] for _ in range(n + 1)]
dp[0][0][0] = 1
answer = 0

for day in range(n):
    for late in range(max_late):
        for absent in range(max_absent):
            cur = dp[day][late][absent]

            if cur == 0:
                continue

            # 출석
            dp[day + 1][late][0] = (dp[day + 1][late][0] + cur) % mod

            # 지각
            if late == 0:
                dp[day + 1][late + 1][0] = (dp[day + 1][late + 1][0] + cur) % mod

            # 결석
            if absent < 2:
                dp[day + 1][late][absent + 1] = (dp[day + 1][late][absent + 1] + cur) % mod

for late in range(max_late):
    for absent in range(max_absent):
        answer = (answer + dp[n][late][absent]) % mod

print(answer)
