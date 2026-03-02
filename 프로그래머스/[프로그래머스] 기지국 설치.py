from math import ceil

def solution(n, stations, w):
    answer = 0
    coverage = w * 2 + 1
    cur = 1 # 전파가 도달하는지 확인하려는 위치 (아파트 1부터 시작)

    for station in stations:
        left_cover = station - w
        empty = left_cover - cur

        # 현재 탐색 위치와 기지국의 왼쪽 커버 범위 사이에 빈 공간이 있는 경우
        # 전부 커버할 수 있을 만큼 기지국 설치
        if empty > 0:
            answer += ceil(empty / coverage)

        # 기지국의 오른쪽 범위까지는 커버되고 있으므로
        # 현재 탐색 위치를 기지국의 오른쪽 커버 범위 바로 다음으로 이동
        cur = station + w + 1

    # 오른쪽에 빈 공간이 남은 경우 처리
    if cur <= n:
        empty = n - cur + 1
        answer += ceil(empty / coverage)

    return answer
