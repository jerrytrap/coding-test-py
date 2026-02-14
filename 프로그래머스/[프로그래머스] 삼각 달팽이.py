def solution(n):
    answer = []
    direction = [(1, 0), (0, 1), (-1, -1)]
    snail = [[0] * n for _ in range(n)]
    cur = (0, 0) # 현재 좌표
    cur_dir = 0 # 현재 방향
    num = 1 # 배열에 채울 숫자
    max_num = n * (n + 1) // 2 # 마지막 번호 = 1 ~ n까지의 합

    def is_available_point(x, y):
        return 0 <= x < n and 0 <= y < n

    def get_next_point(x, y):
        dx, dy = direction[cur_dir % 3]

        return x + dx, y + dy

    while num <= max_num:
        # 현재 좌표에 숫자 채워넣기
        x, y = cur
        snail[x][y] = num

        # 현재 방향을 고려해 다음 위치 계산
        nx, ny = get_next_point(x, y)

        # 유효한 좌표이면서 빈 칸인 경우
        if is_available_point(nx, ny) and snail[nx][ny] == 0:
            cur = (nx, ny)

        # 좌표를 넘어가거나 숫자가 이미 있는 경우
        # 방향 바꾸고 위치 다시 계산
        else:
            cur_dir += 1
            cur = get_next_point(x, y)

        num += 1

    for i in range(n):
        for j in range(i + 1):
            answer.append(snail[i][j])

    return answer
