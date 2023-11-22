from queue import Queue

def solution(n, paths, gates, summits):
    answer = [50001, 10000001]
    graph = [[] for _ in range(n + 1)]
    queue = Queue()
    intensity = [10000001 for _ in range(n + 1)]
    summits = set(summits)

    #그래프 만들기
    for path in paths:
        start, end, weight = path
        graph[start].append((end, weight))
        graph[end].append((start, weight))

    #큐에 시작 지점들을 넣고, intensity를 0으로 지정
    for gate in gates:
        queue.put(gate)
        intensity[gate] = 0

    while not queue.empty():
        start = queue.get()

        #연결된 간선 모두 확인
        for end, weight in graph[start]:
            #산봉우리까지의 경로만 확인하므로, 산봉우리에서 출발하는 간선은 확인하지 않음
            if start in summits:
                continue
            #intensity 갱신 및 큐에 삽입
            if intensity[end] > max(intensity[start], weight):
                intensity[end] = max(intensity[start], weight)
                queue.put(end)

    #intensity가 가장 작으면서, 번호가 가장 작은 산봉우리 구하기
    for summit in summits:
        if answer[1] > intensity[summit]:
            answer = [summit, intensity[summit]]
        elif answer[1] == intensity[summit]:
            if answer[0] > summit:
                answer = [summit, intensity[summit]]

    return answer

ans = solution(7, 	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
print(ans)
