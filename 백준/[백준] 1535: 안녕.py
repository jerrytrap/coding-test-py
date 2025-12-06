import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
j = list(map(int, input().split()))
dp = [0 for _ in range(101)]

for i in range(n):
    life, joy = l[i], j[i]

    for k in range(100, life, -1):
        dp[k] = max(dp[k], dp[k - life] + joy)

print(max(dp[1:]))
