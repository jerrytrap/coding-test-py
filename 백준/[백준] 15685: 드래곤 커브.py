import sys
input = sys.stdin.readline

n = int(input())
left_curve = [1, 2, 3, 0]
board = [[False for _ in range(101)] for _ in range(101)]
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

def is_available_point(x, y):
    return 0 <= x <= 100 and 0 <= y <= 100

# 드래곤 커브를 만들기 위한 진행 방향 구하기
def get_directions(start_dir, gen):
    directions = [start_dir]

    for _ in range(gen):
        next_gen = reversed(list(map(lambda x: left_curve[x], directions)))
        directions.extend(next_gen)

    return directions

# 드래곤 커브 만들기
def dragon_curve(x, y, d, g):
    board[y][x] = True
    directions = get_directions(d, g)

    for i in directions:
        nx, ny = x + dx[i], y + dy[i]
        if not is_available_point(nx, ny):
            return

        board[ny][nx] = True
        x, y = nx, ny

# 정사각형 네 꼭짓점이 모두 드래곤 커브의 일부인 경우 구하기
def count_square():
    cnt = 0

    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
                cnt += 1

    return cnt

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon_curve(x, y, d, g)

print(count_square())