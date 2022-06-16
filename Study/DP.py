# 동적 계획법 - 배낭 문제
def knapsack():
    dp = [[0 for _ in range(maxWeight+1)] for _ in range(rowCount+1)]
    for row in range(1, rowCount+1):
        for col in range(1, maxWeight+1):
            # 물건 무게가 배낭 무게보다 크면, 물건을 넣기 전 무게와 같음
            if weight[row] > col:
                dp[row][col] = dp[row-1][col]
            else:
                value1 = money[row] + dp[row-1][col-weight[row]]  # 물건을 넣기 전 가격 + 물건의 가격
                value2 = dp[row-1][col]  # 물건을 안 넣었을 떄 가격
                dp[row][col] = max(value1, value2)

    return dp[rowCount][maxWeight]


weight = [0, 6, 4, 3, 5]  # 보석 무게
money = [0, 13, 8, 6, 12]  # 보석 가격
maxWeight = 7  # 배낭 최대 무게
rowCount = 4  # 보석 개수
