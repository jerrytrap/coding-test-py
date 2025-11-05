import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m, fuel = map(int, input().split())
board = [input().split() for _ in range(n)]
start = tuple(map(lambda x: int(x) - 1, input().split()))
passenger = deepcopy(board)
goal = deepcopy(board)
remain = m
answer = True
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def is_available_point(x, y):
    return 0 <= x < n and 0 <= y < n

def find_nearest_passenger(start):
    dis = 0
    sx, sy = start

    # 승객이 출발점에 존재
    if passenger[sx][sy] not in ['0', '1']:
        return passenger[sx][sy], sx, sy, dis

    queue = deque([start])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = True

    while queue:
        # 같은 거리인 칸에 존재하는 모든 승객 찾기
        new_queue = deque()
        dis += 1
        passengers = []

        for q in queue:
            x, y = q

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if is_available_point(nx, ny) and board[nx][ny] == '0' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_queue.append((nx, ny))

                    # 승객이 있는 칸이라면 추가
                    if passenger[nx][ny] not in ['0', '1']:
                        passengers.append((passenger[nx][ny], nx, ny))

        # 같은 거리인 칸에 승객이 한 명 이상인 경우 - 행, 열이 작은 순서
        if len(passengers) > 0:
            passengers.sort(key=lambda p: (p[1], p[2]))
            return *passengers[0], dis

        queue = new_queue

    # 승객을 찾을 수 없는 경우
    return None

def move_to_goal(num, start):
    dis = 0
    sx, sy = start

    # 목적지가 출발점에 존재
    if goal[sx][sy] != '0' and num in goal[sx][sy]:
        return sx, sy, dis

    queue = deque([start])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sx][sy] = True

    while queue:
        new_queue = deque()
        dis += 1
        for q in queue:
            x, y = q

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if is_available_point(nx, ny) and board[nx][ny] == '0' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_queue.append((nx, ny))

                    if goal[nx][ny] != '0' and num in goal[nx][ny]:
                        return nx, ny, dis

        queue = new_queue

    # 목적지에 도달할 수 없는 경우
    return None

for i in range(m):
    px, py, gx, gy = map(int, input().split())
    passenger[px - 1][py - 1] = i

    if goal[gx - 1][gy - 1] == '0':
        goal[gx - 1][gy - 1] = [i]
    else:
        goal[gx - 1][gy - 1].append(i)

while remain > 0:
    # 가까운 승객 찾기
    near_info = find_nearest_passenger(start)

    # 승객을 찾을 수 없는 경우 (벽에 막힘)
    if not near_info:
        answer = False
        break

    num, near_x, near_y, near_dis = near_info
    passenger[near_x][near_y] = '0'
    start = (near_x, near_y)

    # 연료 감소
    fuel -= near_dis
    if fuel < 0:
        answer = False
        break

    # 목적지 찾기
    goal_info = move_to_goal(num, start)

    # 목적지를 찾을 수 없는 경우 (벽에 막힘)
    if not goal:
        answer = False
        break

    goal_x, goal_y, g_dis = goal_info
    start = (goal_x, goal_y)

    # 연료 감소
    fuel -= g_dis
    if fuel < 0:
        answer = False
        break

    # 연료 충전 및 남은 승객 감소
    fuel += (g_dis * 2)
    remain -= 1

print(fuel if answer else -1)
