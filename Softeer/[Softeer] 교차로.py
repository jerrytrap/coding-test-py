import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
road_names = ['A', 'B', 'C', 'D']
waiting = dict({'A': False, 'B': False, 'C': False, 'D': False})
road = dict({'A': deque(), 'B': deque(), 'C': deque(), 'D': deque()})
right_road = dict({'A': 'D', 'B': 'A', 'C': 'B', 'D': 'C'})

answer = [-1 for _ in range(n)]
cur_time = 0

for idx in range(n):
    time, pos = input().split()
    time = int(time)
    road[pos].append((idx, time))

while road['A'] or road['B'] or road['C'] or road['D']:
    min_time = 1_000_000_000

    for pos in road_names:
        if road[pos]:
            idx, time = road[pos][0]
            min_time = min(min_time, time)
            if time <= cur_time:
                waiting[pos] = True

    if False not in waiting.values():
        break

    if True not in waiting.values():
        cur_time = min_time
        continue

    for pos in road_names:
        if waiting[pos] and not waiting[right_road[pos]]:
            idx, time = road[pos].popleft()
            answer[idx] = cur_time

    for pos in road_names:
        waiting[pos] = False

    cur_time += 1

for ans in answer:
    print(ans)
