import sys
input = sys.stdin.readline

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 보드 위의 말 위치 정보
board_info = [[[] for _ in range(n)] for _ in range(n)]
# 각 말들의 위치 및 방향 정보
piece_info = []
# 오른쪽, 왼쪽, 위, 아래
dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]
turn = 1

def is_out_of_board(x, y):
    return not(0 <= x < n and 0 <= y < n)

def get_opposite_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def move(i):
    # 이동할 말 위에 올려져 있는 말들 구하기
    def slice(x, y, i):
        idx = board_info[x][y].index(i)
        return board_info[x][y][:idx], board_info[x][y][idx:]

    # 이동할 말 위에 올려져 있는 말들 이동
    def move_upper_pieces(pieces):
        for p in pieces:
            piece_info[p] = (nx, ny, piece_info[p][2])

    # 이동할 칸이 빨간색인 경우
    def do_red():
        prev, next = slice(x, y, i)
        board_info[x][y] = prev
        board_info[nx][ny].extend(reversed(next))
        move_upper_pieces(next)

    # 이동할 칸이 흰색인 경우
    def do_white():
        prev, next = slice(x, y, i)
        board_info[x][y] = prev
        board_info[nx][ny].extend(next)
        move_upper_pieces(next)

    x, y, d = piece_info[i]
    nx, ny = x + dir[d][0], y + dir[d][1]

    # 이동할 칸이 파란색 또는 벽인 경우
    if is_out_of_board(nx, ny) or board[nx][ny] == 2:
        nd = get_opposite_dir(d)
        nx, ny = x + dir[nd][0], y + dir[nd][1]

        # 방향 바꾼 후 다시 이동
        if is_out_of_board(nx, ny) or board[nx][ny] == 2:
            piece_info[i] = (x, y, nd)
        elif board[nx][ny] == 1:
            piece_info[i] = (nx, ny, nd)
            do_red()
        elif board[nx][ny] == 0:
            piece_info[i] = (nx, ny, nd)
            do_white()
    # 이동할 칸이 빨간색인 경우
    elif board[nx][ny] == 1:
        piece_info[i] = (nx, ny, d)
        do_red()
    # 이동할 칸이 흰색인 경우
    elif board[nx][ny] == 0:
        piece_info[i] = (nx, ny, d)
        do_white()

    # 길이 4 이상이면 종료
    if not(is_out_of_board(nx, ny)) and len(board_info[nx][ny]) >= 4:
        return True

    return False

def move_all():
    for i in range(k):
        if move(i):
            return True

    return False

for i in range(k):
    x, y, d = map(int, input().split())
    board_info[x - 1][y - 1].append(i)
    piece_info.append((x - 1, y - 1, d - 1))

while turn <= 1001:
    if move_all():
        break

    turn += 1

print(-1 if turn >= 1001 else turn)