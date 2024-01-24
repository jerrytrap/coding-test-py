import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reversed_graph = [[] for _ in range(n + 1)]
answer = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    reversed_graph[end].append(start)

s, t = map(int, input().split())

def dfs(start, graph, visited):
    if visited[start] == True:
        return
    visited[start] = True

    for next in graph[start]:
        dfs(next, graph, visited)

#S에서 갈 수 있는 지점 탐색
from_s_visited = [False for _ in range(n + 1)]
from_s_visited[t] = True
dfs(s, graph, from_s_visited)

#S로 돌아올 수 있는 지점 탐색
to_s_visited = [False for _ in range(n + 1)]
dfs(s, reversed_graph, to_s_visited)

#T에서 갈 수 있는 지점 탐색
from_t_visited = [False for _ in range(n + 1)]
from_t_visited[s] = True
dfs(t, graph, from_t_visited)

#T로 돌아올 수 있는 지점 탐색
to_t_visited = [False for _ in range(n + 1)]
dfs(t, reversed_graph, to_t_visited)

for i in range(1, n + 1):
    if from_s_visited[i] and from_t_visited[i] and to_s_visited[i] and to_t_visited[i]:
        answer += 1

#S, T 제외
print(answer - 2)