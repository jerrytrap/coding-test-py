from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    start = (0, 0)
    lever = (0, 0)

    #시작 지점, 레버 위치를 미리 저장
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            if maps[i][j] == 'L':
                lever = (i, j)

    #레버까지의 최단 거리 계산, 갈 수 없으면 -1 반환
    lever_dis = bfs(maps, [[False for _ in range(len(maps[0]))] for _ in range(len(maps))], (start[0], start[1], 0), 'L')
    if lever_dis == -1:
        return -1

    #레버에서부터 출구까지 최단 거리 계산, 갈 수 없으면 -1 반환
    end_dis = bfs(maps, [[False for _ in range(len(maps[0]))] for _ in range(len(maps))], (lever[0], lever[1], 0), 'E')
    if end_dis == -1:
        return -1

    return lever_dis + end_dis

def bfs(maps, visited, start, target):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        time = node[2]

        if maps[node[0]][node[1]] == target:
            return time

        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                queue.append((nx, ny, time + 1))
                visited[nx][ny] = True

    return -1
