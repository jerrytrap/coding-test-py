from math import ceil
from collections import deque

def solution(progresses, speeds):
    queue = deque()
    answer = []

    # 기능별 남은 일수 계산
    for idx, progress in enumerate(progresses):
        left = ceil((100 - progress) / speeds[idx])
        queue.append(left)

    while queue:
        left = queue.popleft()
        count = 1 # 한 번에 배포되는 기능의 개수

        # 뒤에 있는 기능이 앞의 기능보다 먼저 끝나는 경우엔 같이 배포되므로 추가로 큐에서 꺼내줌
        while queue and left >= queue[0]:
            queue.popleft()
            count += 1

        answer.append(count)

    return answer
