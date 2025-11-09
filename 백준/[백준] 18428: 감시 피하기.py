import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
classroom = []
empty = []
teachers = []
answer = False
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def is_available_point(x, y):
    return 0 <= x < n and 0 <= y < n

def check(start):
    x, y = start
    wall = [False, False, False, False]  # 탐색 방향이 벽에 막혔는지 여부

    for dis in range(1, 7):
        for i in range(4):
            if wall[i]:
                continue

            nx, ny = x + dx[i] * dis, y + dy[i] * dis

            if is_available_point(nx, ny):
                if classroom[nx][ny] == 'O':
                    wall[i] = True
                elif classroom[nx][ny] == 'S':
                    return False

    return True

def check_all():
    for teacher in teachers:
        if not check(teacher):
            return False

    return True

for i in range(n):
    row = input().split()
    classroom.append(row)

    for j in range(n):
        if row[j] == 'X':
            empty.append((i, j))
        elif row[j] == 'T':
            teachers.append((i, j))

# 벽을 설치할 수 있는 모든 조합 확인
for combination in combinations(empty, 3):
    for x, y in combination:
        classroom[x][y] = 'O'

    if check_all():
        answer = True
        break

    for x, y in combination:
        classroom[x][y] = 'X'

print("YES" if answer else "NO")
