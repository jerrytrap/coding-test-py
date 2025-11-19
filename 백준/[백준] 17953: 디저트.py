import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mood = [list(map(int, input().split())) for _ in range(m)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    dp[0][i] = mood[i][0]

# 디저트가 한 종류면 매일 같은 것만 먹어야함
if m == 1:
    for day in range(1, n):
        dp[day][0] = dp[day - 1][0] + mood[0][day] // 2

    print(dp[n - 1][0])
else:
    for day in range(1, n):
        # 전 날 만족감이 최대인 경우 구하기
        # 이 경우와 오늘 먹을 디저트가 같으면 만족감이 떨어지므로 다음 순위도 미리 구해놓음
        find_max = [(dp[day - 1][dessert], dessert) for dessert in range(m)]
        find_max.sort(reverse=True)
        first, max_idx = find_max[0]
        second, _ = find_max[1]

        for dessert in range(m):
            # 전날과 오늘 같은 디저트를 먹는 경우
            same = dp[day - 1][dessert] + mood[dessert][day] // 2

            # 전날과 오늘 다른 디저트를 먹는 경우
            if dessert == max_idx:
                diff = second + mood[dessert][day]
            else:
                diff = first + mood[dessert][day]

            dp[day][dessert] = max(same, diff)

    print(max(dp[n - 1]))
