from collections import defaultdict

def solution(N, stages):
    answer = []
    fail = defaultdict(int)
    total = len(stages)

    for stage in stages:
        fail[stage] += 1

    for i in range(1, N + 1):
        # i번 스테이지에 도달한 유저가 없는 경우
        # 실패율 = 0
        if fail[i] == 0:
            answer.append((i, 0))
        else:
            answer.append((i, fail[i] / total))

            # 현재 스테이지에서 실패한 유저는 제외(다음 스테이지에 도전할 수 없으므로)
            total -= fail[i]

    answer.sort(key=lambda x: -x[1])
    return [ans[0] for ans in answer]
