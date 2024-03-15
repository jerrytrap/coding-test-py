import sys
from collections import deque
from math import inf
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[False, False] for _ in range(m)] for _ in range(n)]
distances = [[inf for _ in range(m)] for _ in range(n)]

def is_point_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y, False, 1)])

    while queue:
        x, y, crashed, dist = queue.popleft()
        distances[x][y] = min(distances[x][y], dist)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #방문 표시를 할 때, 벽을 부수고 왔는지 아닌지를 나누어 체크함
            #visited[x][y] - index 0: 안 부수고 방문, index 1: 부수고 방문
            if is_point_valid(nx, ny):
                #벽이 아닌 경우 - 이전까지의 벽 파괴 여부를 그대로 갱신해줌
                if board[nx][ny] == '0':
                    #벽을 이미 한 번 부수고 온 경우
                    if crashed and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, True, dist + 1))

                    #벽을 안 부수고 온 경우
                    elif not crashed and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        queue.append((nx, ny, False, dist + 1))

                #벽인 경우
                else:
                    #벽을 아직 파괴하지 않은 경우 부수고 이동
                    if not crashed and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, True, dist + 1))

for _ in range(n):
    board.append(input().strip())

visited[0][0][0] = True
bfs(0, 0)

answer = distances[n - 1][m - 1]
if answer == inf:
    print(-1)
else:
    print(answer)