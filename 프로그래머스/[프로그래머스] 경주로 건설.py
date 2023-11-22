from collections import deque

def solution(board):
    answer = []
    row = len(board)
    col = len(board[0])
    area = row * col
    distance = [[[{'UP' : area+1, 'DOWN' : area+1, 'LEFT' : area+1, 'RIGHT' : area+1} for _ in range(area+1)] for _ in range(col)] for _ in range(row)]
    visited = [[[{'UP' : False, 'DOWN' : False, 'LEFT' : False, 'RIGHT' : False} for _ in range(area+1)] for _ in range(col)] for _ in range(row)]
    queue = deque([(0, 0, 0, 'DOWN'), (0, 0, 0, 'RIGHT')])

    #시작 지점 설정
    distance[0][0][0]['DOWN'] = 0
    distance[0][0][0]['RIGHT'] = 0
    visited[0][0][0]['DOWN'] = True
    visited[0][0][0]['RIGHT'] = True

    def move_next(nx, ny, is_corner, corner, new_dir):
        #시작 지점은 바라보는 방향과 진행 방향이 달라도 corner가 생기지 않으므로 corner수를 증가시키지 않음
        new_corner = corner + 1 if is_corner else corner

        #최대 corner수 = 칸 수
        if (0 <= nx < row and 0 <= ny < col
                and corner < area
                and not visited[nx][ny][new_corner][new_dir]
                and not board[nx][ny]):
            distance[nx][ny][new_corner][new_dir] = min(distance[nx][ny][new_corner][new_dir], distance[x][y][corner][dir] + 1)
            visited[nx][ny][new_corner][new_dir] = True
            queue.append((nx, ny, new_corner, new_dir))

    def move_straight(x, y, corner, dir):
        nx = x
        ny = y

        if dir == 'UP':
            nx -= 1
        elif dir == 'DOWN':
            nx += 1
        elif dir == 'LEFT':
            ny -= 1
        else:
            ny += 1

        move_next(nx, ny, False, corner, dir)

    def move_left(x, y, corner, dir):
        nx = x
        ny = y
        is_corner = True if x > 0 or y > 0 else False

        if dir == 'UP':
            ny -= 1
            new_dir = 'LEFT'
        elif dir == 'DOWN':
            ny += 1
            new_dir = 'RIGHT'
        elif dir == 'LEFT':
            nx += 1
            new_dir = 'DOWN'
        else:
            nx -= 1
            new_dir = 'UP'

        move_next(nx, ny, is_corner, corner, new_dir)

    def move_right(x, y, corner, dir):
        nx = x
        ny = y
        is_corner = True if x > 0 or y > 0 else False

        if dir == 'UP':
            ny += 1
            new_dir = 'RIGHT'
        elif dir == 'DOWN':
            ny -= 1
            new_dir = 'LEFT'
        elif dir == 'LEFT':
            nx -= 1
            new_dir = 'UP'
        else:
            nx += 1
            new_dir = 'DOWN'

        move_next(nx, ny, is_corner, corner, new_dir)

    #BFS
    while queue:
        x, y, corner, dir = queue.popleft()

        move_straight(x, y, corner, dir)
        move_left(x, y, corner, dir)
        move_right(x, y, corner, dir)

    #corner수 별로 최소 비용을 확인하고 그 중에서 가장 작은 값을 구한다.
    for corner, dis in enumerate(distance[row-1][col-1]):
        min_dis = min(dis.values())
        if min_dis <= area:
            answer.append(min_dis * 100 + corner * 500)

    return min(answer)