def solution(commands):
    answer = []
    table_size = 50
    table = [['EMPTY' for _ in range(table_size+1)] for _ in range(table_size+1)]
    merged = [[(i, j) for j in range(table_size+1)] for i in range(table_size+1)]

    def change_values(value1, value2):
        for i in range(1, table_size+1):
            for j in range(1, table_size+1):
                if table[i][j] == value1:
                    table[i][j] = value2

    def merge_table(r1, c1, r2, c2):
        x1, y1 = merged[r1][c1]
        x2, y2 = merged[r2][c2]

        if table[x1][y1] == 'EMPTY' and table[x2][y2] != 'EMPTY':
            value = table[x2][y2]
        else:
            value = table[x1][y1]

        table[x1][y1] = value

        #병합 정보 바꿔주기 - (r2, c2)와 병합된 셀을 전부 (r1, c1)와 병합된 셀로 설정
        for i in range(1, table_size+1):
            for j in range(1, table_size+1):
                if merged[i][j] == (x2, y2):
                    merged[i][j] = (x1, y1)

    def unmerge_table(r, c):
        x, y = merged[r][c]
        #선택된 좌표만 값 바꿔주기
        table[r][c] = table[x][y]

        # 병합 정보 바꿔주기 - (r, c)와 병합된 셀을 전부 원래 셀 좌표로 설정
        for i in range(1, table_size+1):
            for j in range(1, table_size+1):
                if merged[i][j] == (x, y):
                    merged[i][j] = (i, j)
                    table[i][j] = 'EMPTY'

    for command in commands:
        command_list = command.split()
        type = command_list[0]

        if type == 'UPDATE':
            if len(command_list) == 4:
                r, c, value = int(command_list[1]), int(command_list[2]), command_list[3]
                x, y = merged[r][c]
                table[x][y] = value
            else:
                value1, value2 = command_list[1:3]
                change_values(value1, value2)
        elif type == 'MERGE':
            r1, c1, r2, c2 = map(int, command_list[1:5])
            merge_table(r1, c1, r2, c2)
        elif type == 'UNMERGE':
            r, c = map(int, command_list[1:3])
            unmerge_table(r, c)
        else:
            r, c = map(int, command_list[1:3])
            x, y = merged[r][c]
            answer.append(table[x][y])

    return answer
