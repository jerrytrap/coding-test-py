import math

def solution(alp, cop, problems):
    target_alp = alp
    target_cop = cop

    #문제를 모두 풀 수 있는 목표 알고력과 코딩력 구하기
    for alp_req, cop_req, _, _, _ in problems:
        target_alp = max(target_alp, alp_req)
        target_cop = max(target_cop, cop_req)

    dp = [[math.inf for _ in range(target_cop + 1)] for _ in range(target_alp + 1)]
    dp[alp][cop] = 0

    #목표 알고력과 코딩력이 될 때까지 dp 테이블 채우기
    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):
            #알고력을 1 늘리는 경우
            if a < target_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            #코딩력을 1 늘리는 경우
            if c < target_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            #문제를 푸는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    new_a = min(a + alp_rwd, target_alp)
                    new_c = min(c + cop_rwd, target_cop)

                    dp[new_a][new_c] = min(dp[new_a][new_c], dp[a][c] + cost)

    return dp[target_alp][target_cop]