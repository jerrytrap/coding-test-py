def solution(rows, columns, queries):
    answer = []
    table = [[(r * columns) + c + 1 for c in range(columns)] for r in range(rows)]

    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        tmp = table[r1][c2]
        min_val = tmp

        # 위
        for c in range(c2, c1, -1):
            table[r1][c] = table[r1][c - 1]
            min_val = min(min_val, table[r1][c - 1])

        # 왼쪽
        for r in range(r1, r2):
            table[r][c1] = table[r + 1][c1]
            min_val = min(min_val, table[r + 1][c1])

        # 아래
        for c in range(c1, c2):
            table[r2][c] = table[r2][c + 1]
            min_val = min(min_val, table[r2][c + 1])

        # 오른쪽
        for r in range(r2, r1, -1):
            table[r][c2] = table[r - 1][c2]
            min_val = min(min_val, table[r - 1][c2])

        table[r1 + 1][c2] = tmp
        answer.append(min_val)

    return answer
