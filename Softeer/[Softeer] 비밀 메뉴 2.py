import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
menu1 = list(map(int, input().split()))
menu2 = list(map(int, input().split()))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
answer = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if menu1[i - 1] == menu2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])

print(answer)