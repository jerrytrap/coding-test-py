def solution(n):
    answer = 0
    queen = [-1] * n

    def is_safe(row, col):
        for r in range(row):
            # col 열에 퀸이 이미 있는 경우
            # (row, col) 칸의 대각선에 퀸이 이미 있는 경우
            if queen[r] == col or abs(r - row) == abs(queen[r] - col):
                return False

        return True

    def dfs(row):
        nonlocal answer

        if row == n:
            answer += 1
            return

        for col in range(n):
            # 퀸을 배치할 수 있는 경우에만 추가로 탐색
            if is_safe(row, col):
                queen[row] = col
                dfs(row + 1)

    dfs(0)
    return answer