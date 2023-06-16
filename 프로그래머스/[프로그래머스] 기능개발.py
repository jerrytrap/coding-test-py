def solution(progresses, speeds):
    days = []  # 기능별 남은 일수
    queue = []
    answer = []

    # 기능별 남은 일수 계산
    for idx, progress in enumerate(progresses):
        day = (100 - progress) // speeds[idx]

        if progress + (day * speeds[idx]) < 100:
            day += 1
        days.append(day)

    # 남은 일수를 기준으로 언제 배포되는지 계산
    queue.append(days[0])
    for i in range(1, len(days)):
        if queue[0] >= days[i]:
            queue.append(days[i])
        else:
            answer.append(len(queue))
            queue.clear()
            queue.append(days[i])

    # 반복이 끝난 뒤 큐에 작업할 기능이 아직 남아있다면 추가
    if len(queue) > 0:
        answer.append(len(queue))
    return answer
