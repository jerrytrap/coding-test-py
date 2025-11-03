import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [input().strip().split() for _ in range(n)]
inactives = []
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
answer = 10e9

def is_valid_point(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(starts):
    queue = deque([(x, y, 0) for x, y in starts])
    board = copy.deepcopy(lab)
    max_time = -1
    visited = [[False for _ in range(n)] for _ in range(n)]

    for x, y in starts:
        visited[x][y] = True
        board[x][y] = 0

    while queue:
        new_queue = deque()

        # 같은 시간에 바이러스들을 동시에 확산시켜야 하므로
        # 현재 큐에 있는 데이터를 한 번에 확인
        for x, y, time in queue:
            for dx, dy in dir:
                nx = x + dx
                ny = y + dy

                if is_valid_point(nx, ny) and not visited[nx][ny]:
                    # 방문하지 않은 빈 칸인 경우
                    # 확산된 시간 기록
                    if board[nx][ny] == '0':
                        new_queue.append((nx, ny, time + 1))
                        visited[nx][ny] = True
                        board[nx][ny] = time + 1

                    # 바이러스가 위치한 칸인 경우
                    elif board[nx][ny] == -2:
                        new_queue.append((nx, ny, time + 1))
                        visited[nx][ny] = True

        queue = new_queue

    # 확산되지 않은 빈 칸이 있는지 확인
    for row in board:
        if '0' in row:
            return 10e9
        max_time = max(max_time, max(row))

    return max_time

# 비활성 바이러스 위치 찾기
# 바이러스를 퍼뜨린 시간을 편하게 계산하기 위해 벽과 바이러스 칸을 정수로 변경
for i in range(n):
    for j in range(n):
        if lab[i][j] == '2':
            lab[i][j] = -2
            inactives.append((i, j))
        elif lab[i][j] == '1':
            lab[i][j] = -1

#바이러스를 M개 활성화시키는 조합 확인
for actives in combinations(inactives, m):
    answer = min(answer, bfs(actives))

print(answer if answer != 10e9 else -1)