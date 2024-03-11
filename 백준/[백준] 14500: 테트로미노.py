import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]
answer = 0
board_max_value = 0

for _ in range(n):
    row = list(map(int, input().split()))
    board_max_value = max(board_max_value, max(row))
    board.append(row)

def is_pos_valid(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y, depth, sum):
    global answer
    if sum + (4 - depth) * board_max_value <= answer:
        return

    if depth == 4:
        answer = max(answer, sum)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if is_pos_valid(nx, ny) and not visited[nx][ny]:
            if depth == 2:
                visited[nx][ny] = True
                dfs(x, y, depth + 1, sum + board[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, sum + board[nx][ny])
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)