import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    now = 0 # 현재 시점
    cur_job = 0 # 현재 작업
    prev_end = -1 # 이전 작업의 시작 시점
    heap = []

    while cur_job < n:
        # 현재 작업 시작 이후에 들어오는 작업을 확인
        for job in jobs:
            start, duration = job

            # 현재 시점 이전에 새 작업이 들어왔었다면 우선순위 큐에 넣어두기
            if prev_end < start <= now:
                heapq.heappush(heap, (duration, start))

        # 큐에 작업이 대기 중인 경우
        # 가장 소요시간이 적은 작업 처리
        if heap:
            duration, start = heapq.heappop(heap)
            prev_end = now
            now += duration
            answer += (now - start)
            cur_job += 1

        # 큐에 대기 중인 작업이 없다면 시간이 흐름
        else:
            now += 1

    return answer // n
