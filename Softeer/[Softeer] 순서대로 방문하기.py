import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
points = []
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def set_board():
    for _ in range(n):
        board.append(list(map(int, input().split())))

def set_visit_points():
    for _ in range(m):
        x, y = map(int, input().split())
        points.append((x - 1, y - 1))

def set_start_point():
    start_x, start_y = points[0]
    visited[start_x][start_y] = True

def dfs(point, visit, visited):
    global answer
    x, y = point

    #올바른 순서로 방문한 경우, 다음에 방문해야 할 지점 설정
    if (x, y) == points[visit]:
        visit += 1

    #주어진 지점을 모두 방문한 경우
    if visit == len(points):
        answer += 1
        return

    #다른 지점을 먼저 방문한 경우는 탐색하지 않음
    if (x, y) in points[visit + 1:]:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs((nx, ny), visit, visited)
            visited[nx][ny] = False

set_board()
set_visit_points()
set_start_point()

dfs(points[0], 0, visited)
print(answer)