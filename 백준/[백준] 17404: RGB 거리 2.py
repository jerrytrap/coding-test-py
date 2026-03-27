import sys
from math import inf
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
answer = inf

# 첫 번째 집을 빨강, 초록, 파랑으로 칠하고 시작
for start_color in range(3):
    # dp[i][j]: i번째 집을 j로 칠할 때 최소 비용
    dp = [[0] * 3 for _ in range(n)]

    # 첫 번째 집을 칠하는 색깔에 해당하는 비용 기록 (나머지 두 색은 INF로 처리)
    for color in range(3):
        if color == start_color:
            dp[0][color] = cost[0][color]
        else:
            dp[0][color] = inf

    # 두 번째 집부터 마지막 집까지 비용 체크
    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    # 마지막 집과 첫 번째 집을 칠한 색이 서로 같으면 조건을 만족하지 않으므로 제외
    for color in range(3):
        if color != start_color:
            answer = min(answer, dp[-1][color])

print(answer)
