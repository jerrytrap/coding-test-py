import sys
input = sys.stdin.readline

t = int(input())
k = int(input())

coins = []
for _ in range(k):
    p, n = map(int, input().split())
    coins.append((p, n))

dp = [0 for _ in range(t + 1)]
dp[0] = 1

for value, count in coins:
    new_dp = dp[:]
    for money in range(t + 1):
        if dp[money] == 0:
            continue

        for used in range(1, count + 1):
            next = money + used * value
            if next > t:
                break
            new_dp[next] += dp[money]

    dp = new_dp

print(dp[t])
