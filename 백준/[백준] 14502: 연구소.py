from collections import deque
import copy
from itertools import combinations

def bfs(maps):
    global answer
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                queue.append((nx, ny))

    answer = max(answer, count_safe(maps))

#안전 구역 개수 세기
def count_safe(maps):
    cnt = 0
    for i in range(n):
        cnt += maps[i].count(0)
    return cnt

n, m = map(int, input().split())
maps = []

answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
safe = []
virus = []
for i in range(n):
    maps.append(list(map(int, input().split())))

#안전 구역과 바이러스 구역의 위치 미리 저장
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            safe.append((i, j))
        elif maps[i][j] == 2:
            virus.append((i, j))

#안전 구역 중에서 3가지를 뽑는 조합을 전부 확인
for comb in combinations(safe, 3):
    #벽을 세우고 바이러스를 퍼뜨리면 원래 지도를 활용할 수 없으므로 복사해서 사용
    maps_with_wall = copy.deepcopy(maps)

    for i, j in comb:
        maps_with_wall[i][j] = 1
    bfs(maps_with_wall)

print(answer)
