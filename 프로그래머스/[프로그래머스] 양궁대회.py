def solution(n, info):
    answer = [-1]
    max_diff = 0

    def get_score(scores):
        apeach = 0
        ryan = 0

        for i in range(11):
            if info[i] == 0 and scores[i] == 0:
                continue

            if info[i] >= scores[i]:
                apeach += (10 - i)
            else:
                ryan += (10 - i)

        return apeach, ryan

    def dfs(arrow, idx, scores):
        nonlocal answer
        nonlocal max_diff

        # 과녁 점수를 모두 탐색한 경우
        if idx == 11:
            # 화살을 전부 사용해야 하므로 화살이 남았다면 모두 0에 쏘기
            scores[10] += arrow

            apeach, ryan = get_score(scores)

            # 라이언이 이기는 경우
            if apeach < ryan:
                diff = ryan - apeach

                # 점수 차이가 더 큰 경우 갱신
                if diff > max_diff:
                    max_diff = diff
                    answer = scores[:]

                # 점수 차이가 같은 경우 낮은 점수를 많이 맞춘 경우에만 갱신
                elif diff == max_diff:
                    if scores[::-1] > answer[::-1]:
                        answer = scores[:]

            scores[10] -= arrow
            return

        req_arrow = info[idx] + 1

        # 현재 과녁에 화살을 사용해서 점수를 얻을 수 있는 경우
        if arrow >= req_arrow:
            scores[idx] = req_arrow
            dfs(arrow - req_arrow, idx + 1, scores)
            scores[idx] = 0

        # 현재 과녁에서는 점수를 먹지 않는 경우
        dfs(arrow, idx + 1, scores)

    dfs(n, 0, [0] * 11)
    return answer
