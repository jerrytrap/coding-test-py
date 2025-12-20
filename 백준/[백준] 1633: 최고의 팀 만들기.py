import sys

players = []
for line in sys.stdin:
    players.append(tuple(map(int, line.split())))

dp = [[-1e9 for _ in range(16)] for _ in range(16)]
dp[0][0] = 0

for w, b in players:
    new_dp = [row[:] for row in dp]

    for i in range(16):
        for j in range(16):
            if dp[i][j] == -1e9:
                continue

            if i < 15:
                new_dp[i + 1][j] = max(new_dp[i + 1][j], dp[i][j] + w)

            if j < 15:
                new_dp[i][j + 1] = max(new_dp[i][j + 1], dp[i][j] + b)

    dp = new_dp

print(dp[15][15])
