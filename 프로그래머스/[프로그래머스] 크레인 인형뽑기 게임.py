def solution(board, moves):
    answer = 0
    n = len(board)
    board_info = [[] for _ in range(n + 1)]
    bucket = []

    # board를 스택 형태로 변경
    for j in range(n):
        # 밑에 있는 인형이 나중에 나와야 하므로 역순으로 삽입해줌
        for i in range(n - 1, -1, -1):
            if board[i][j] != 0:
                board_info[j + 1].append(board[i][j])

    for move in moves:
        # 인형이 있는 경우에만
        if board_info[move]:
            doll = board_info[move].pop()

            # 같은 모양 인형 두 개가 연속해서 쌓이는 경우
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)

    return answer
