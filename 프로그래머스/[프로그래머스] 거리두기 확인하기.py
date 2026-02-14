from collections import deque

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def find_candidates(place):
    candidates = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                candidates.append((i, j, 0))

    return candidates

def is_available_point(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def bfs(place, candidates):
    for candidate in candidates:
        visited = [[False] * 5 for _ in range(5)]
        start_x, start_y, _ = candidate
        visited[start_x][start_y] = True
        queue = deque([candidate])

        while queue:
            x, y, dis = queue.popleft()

            # 4방향 BFS 수행
            dis += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if is_available_point(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True

                    # 거리 2 이내에 응시자가 있는 경우
                    if place[nx][ny] == 'P' and dis <= 2:
                        return 0

                    # 거리 1인 칸이 빈 공간인 경우
                    # 다음 칸 탐색을 위해 큐에 삽입
                    if place[nx][ny] == 'O' and dis == 1:
                        queue.append((nx, ny, dis))

    return 1

def solution(places):
    answer = []

    for place in places:
        answer.append(bfs(place, find_candidates(place)))

    return answer
