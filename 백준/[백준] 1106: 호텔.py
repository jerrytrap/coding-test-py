import sys
input = sys.stdin.readline

c, n = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(n)]
max_c = 1000
max_num = 100
dp = [1e9 for _ in range(max_c + max_num + 1)]
dp[0] = 0

# 적어도 C명 늘린다는 것은, C명을 넘어가도 된다는 의미
# C는 최대 1000, 늘릴 수 있는 고객의 수 최댓값은 100이므로, 1100까지는 확인해줘야 함
for i in range(1, max_c + max_num + 1):
    for cost, num in info:
        if i - num >= 0:
            dp[i] = min(dp[i], dp[i - num] + cost)

print(min(dp[c:]))
