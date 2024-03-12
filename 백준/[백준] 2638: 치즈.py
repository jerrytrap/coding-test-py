import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

def is_point_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def is_board_empty():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False

    return True

def remove_cheese(visited):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j].count(True) >= 2:
                board[i][j] = 0

def bfs():
    visited = [[[False, False, False, False] for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if board[x][y] == 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_point_valid(nx, ny) and not visited[nx][ny][i]:
                visited[nx][ny][i] = True
                if board[x][y] == 0:
                    queue.append((nx, ny))

    remove_cheese(visited)

while not is_board_empty():
    bfs()
    answer += 1

print(answer)
