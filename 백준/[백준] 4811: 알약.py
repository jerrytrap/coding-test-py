import sys
input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]

# 한 조각이 없으면 반 조각을 먹는 방법 1가지만 존재
for h in range(31):
    dp[0][h] = 1

for w in range(1, 31):
    for h in range(30):
        # 반 조각이 없으면 한 조각을 반으로 쪼개 먹음
        if h == 0:
            dp[w][h] = dp[w - 1][h + 1]
        # 반 조각이 있으면, 한 조각을 반으로 쪼개 먹거나 반 조각을 먹을 수 있음
        else:
            dp[w][h] = dp[w - 1][h + 1] + dp[w][h - 1]

while True:
    n = int(input())
    if n == 0:
        break

    # 한 조각 n개, 반 조각 0개로 시작
    print(dp[n][0])
