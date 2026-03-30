import sys
from math import inf
input = sys.stdin.readline

queries = list(map(int, input().split()))
queries.pop() # 마지막 입력 0 제외
n = len(queries)
dp = [[inf] * 5 for _ in range(5)]
dp[0][0] = 0 # 양 발 모두 가운데에서 시작

# 발을 이동하는 비용 계산
def get_cost(start, end):
    # 발이 시작 지점에 있는 경우
    if start == 0:
        return 2

    # 발을 움직이지 않고 밟는 경우
    elif start == end:
        return 1

    # 반대 지점을 밟는 경우
    elif abs(start - end) == 2:
        return 4

    # 인접한 지점을 밟는 경우
    else:
        return 3

for query in queries:
    next_dp = [[inf] * 5 for _ in range(5)]

    for left in range(5):
        for right in range(5):
            # 가능하지 않은 왼발과 오른발 상태 제외
            if dp[left][right] == inf:
                continue

            # 오른발이 있는 곳을 왼발로 밟지 않는 경우 -> 왼발 움직이기
            if query != right:
                next_dp[query][right] = min(next_dp[query][right], dp[left][right] + get_cost(left, query))

            # 왼발이 있는 곳을 오른발로 밟지 않는 경우 -> 오른발 움직이기
            if query != left:
                next_dp[left][query] = min(next_dp[left][query], dp[left][right] + get_cost(right, query))

    dp = next_dp

print(min(map(min, dp)))
