import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
near = [[(0, 0) for _ in range(m)] for _ in range(n)]  # 인접한 빈 공간에 대한 정보
answer = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
id = 1  # 인접한 빈 공간 별로 매길 번호

def is_available_point(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    nears = [start]
    result = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if is_available_point(nx, ny) and not visited[nx][ny] and board[nx][ny] == '0':
                visited[nx][ny] = True
                queue.append((nx, ny))
                nears.append((nx, ny))
                result += 1

    # 인접한 공간을 모두 찾았다면 이동할 수 있는 칸의 개수 저장
    for x, y in nears:
        near[x][y] = (id, result)

for i in range(n):
    for j in range(m):
        if board[i][j] == '0' and not visited[i][j]:
            bfs((i, j))
            id += 1

for x in range(n):
    for y in range(m):
        if board[x][y] == '1':
            ans = 1
            ids = []

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if is_available_point(nx, ny):
                    id, value = near[nx][ny]

                    # 인접한 빈 공간이 중복으로 체크하는 경우 방지
                    if id not in ids:
                        ans += value
                        ids.append(id)

            answer[x][y] = ans % 10

for ans in answer:
    print(''.join(map(str, ans)))
