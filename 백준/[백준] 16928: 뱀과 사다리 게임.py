import sys
from collections import deque
from math import inf
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = dict()
snake = dict()
dice_count = [inf for _ in range(101)]
dice_count[1] = 0

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

def bfs(start):
    queue = deque([start])

    while True:
        point = queue.popleft()
        if point == 100:
            break

        for i in range(1, 7):
            new_point = point + i
            if new_point > 100:
                continue

            if new_point in ladder.keys():
                new_point = ladder[new_point]
            elif new_point in snake.keys():
                new_point = snake[new_point]

            if dice_count[new_point] > dice_count[point]:
                dice_count[new_point] = dice_count[point] + 1
                queue.append(new_point)

    return dice_count[100]

print(bfs(1))