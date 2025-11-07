import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
start = None
shark_size = 2
time = 0
cur_eat = 0 # 현재까지 먹은 물고기(상어 크기 증가 시 초기화)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_available_point(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(start):
    global time
    global shark_size
    global cur_eat
    queue = deque([start])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    distance = 0
    can_eat = []

    while queue:
        distance += 1
        new_queue = deque()

        for x, y in queue:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if is_available_point(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True

                    # 빈 칸이거나, 물고기 크기가 상어 크기보다 같거나 작은 경우 -> 지나갈 수 있음
                    if board[nx][ny] == 0 or board[nx][ny] == shark_size:
                        new_queue.append((nx, ny))

                    # 물고기 크기가 상어 크기보다 작은 경우 -> 먹을 수 있음
                    if board[nx][ny] != 0 and board[nx][ny] < shark_size:
                        can_eat.append((nx, ny, board[nx][ny]))

        # 먹을 수 있는 물고기가 1개 이상인 경우
        if len(can_eat) > 0:
            can_eat.sort(key=lambda a: (a[0], a[1]))
            time += distance
            cur_eat += 1

            # 먹은 물고기 수와 상어 크기가 같다면 상어 크기 1 증가
            if shark_size == cur_eat:
                shark_size += 1
                cur_eat = 0

            # 이동할 좌표 반환
            return (can_eat[0][0], can_eat[0][1])

        queue = new_queue

    return None

for r in range(n):
    row = list(map(int, input().split()))

    if 9 in row:
        c = row.index(9)
        start = (r, c)

    board.append(row)

while True:
    new_pos = bfs(start)

    # 먹을 수 있는 물고기가 더 이상 없는 경우
    if not new_pos:
        break

    board[start[0]][start[1]] = 0
    board[new_pos[0]][new_pos[1]] = 9
    start = new_pos

print(time)