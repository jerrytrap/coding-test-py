import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dice = [[0, 2, 0],
        [4, 1, 3],
        [0, 5, 0],
        [0, 6, 0]]
score = 0
cur_pos = (0, 0)
cur_dir = "east"
dir_point = {"east": (0, 1), "west": (0, -1), "south": (1, 0), "north": (-1, 0)}
clockwise = {"east": "south", "west": "north", "south": "west", "north": "east"}
counterclockwise = {"east": "north", "west": "south", "south": "east", "north": "west"}
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def is_available_point(x, y):
    return 0 <= x < n and 0 <= y < m

def reverse_dir(dir):
    global cur_dir

    if dir == "east":
        cur_dir = "west"
    elif dir == "west":
        cur_dir = "east"
    elif dir == "south":
        cur_dir = "north"
    else:
        cur_dir = "south"

def roll():
    global cur_dir, cur_pos
    x, y = cur_pos
    nx, ny = x + dir_point[cur_dir][0], y + dir_point[cur_dir][1]

    # 벽인 경우 방향을 반대로 바꾸고 다시 굴리기
    # 가로, 세로 길이가 모두 2 이상이므로 양쪽 모두 벽인 경우는 없음
    if not is_available_point(nx, ny):
        reverse_dir(cur_dir)
        roll()
        return

    # 현재 방향에 따라 주사위 굴리기
    if cur_dir == "east":
        roll_east()
    elif cur_dir == "west":
        roll_west()
    elif cur_dir == "south":
        roll_south()
    else:
        roll_north()

    # 칸의 점수와 주사위 아랫면 수를 비교한 뒤 조건에 맞게 방향 바꿔주기
    if dice[3][1] > board[nx][ny]:
        cur_dir = clockwise[cur_dir]
    elif dice[3][1] < board[nx][ny]:
        cur_dir = counterclockwise[cur_dir]

    cur_pos = (nx, ny)

def roll_east():
    temp = dice[3][1]
    dice[3][1] = dice[1][2]
    dice[1][2] = dice[1][1]
    dice[1][1] = dice[1][0]
    dice[1][0] = temp

def roll_west():
    temp = dice[3][1]
    dice[3][1] = dice[1][0]
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] = temp

def roll_south():
    temp = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = temp

def roll_north():
    temp = dice[3][1]
    dice[3][1] = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] = temp

# 현재 칸의 점수와 같은 점수인 칸을 모두 탐색
def bfs(start):
    queue = deque([start])
    visited = [[False for _ in range(m)] for _ in range(n)]
    sx, sy = start
    visited[sx][sy] = True
    score = board[sx][sy]
    spaces = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if is_available_point(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True

                if board[nx][ny] == score:
                    queue.append((nx, ny))
                    spaces += 1

    return score * spaces

for _ in range(k):
    roll()
    score += bfs(cur_pos)

print(score)
