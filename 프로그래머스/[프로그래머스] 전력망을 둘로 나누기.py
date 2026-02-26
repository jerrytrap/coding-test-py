from collections import deque

def solution(n, wires):
    answer = n + 1
    graph = [set() for _ in range(n + 1)]

    def add_edges(start, end):
        graph[start].add(end)
        graph[end].add(start)

    def remove_edges(start, end):
        graph[start].remove(end)
        graph[end].remove(start)

    def bfs():
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        network = 1

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    network += 1

        return network

    for start, end in wires:
        add_edges(start, end)

    for start, end in wires:
        remove_edges(start, end)

        network1 = bfs()
        network2 = n - network1
        answer = min(answer, abs(network1 - network2))

        add_edges(start, end)

    return answer
