import sys
input = sys.stdin.readline

# N, M, H
col, input_rows, row = map(int, input().split())
ladders = [[False for _ in range(col - 1)] for _ in range(row)]
answer = 4

# 시작과 끝이 일치하는 세로선의 개수 체크
def count_match_lines():
    match = 0
    for j in range(col):
        current = j
        for i in range(row):
            if current < col - 1 and ladders[i][current]:
                current += 1
            elif current > 0 and ladders[i][current - 1]:
                current -= 1

        if current is j:
            match += 1

    return match

# DFS
def dfs(line_cnt, max_line_cnt):
    global answer

    # 이미 정답이 나왔다면 더 탐색하지 않고 종료
    if answer < 4:
        return

    match_cnt = count_match_lines()

    # 가로선을 최대로 그어도 정답이 나올 수 없다면 더 탐색하지 않고 종료
    if match_cnt + (max_line_cnt - line_cnt) * 2 < col:
        return

    # 가로선을 모두 그었을 때 정답인 경우라면 정답 갱신
    if line_cnt == max_line_cnt and match_cnt == col:
        answer = line_cnt
        return

    for i in range(row):
        for j in range(col - 1):
            # 가로선을 인접하게 만들 수 없으므로 제외
            if (j > 0 and ladders[i][j - 1]) or ladders[i][j] or (j < col - 2 and ladders[i][j + 1]):
                continue

            ladders[i][j] = True
            dfs(line_cnt + 1, max_line_cnt)
            ladders[i][j] = False


for _ in range(input_rows):
    a, b = map(int, input().split())
    ladders[a - 1][b - 1] = True

# 가로선을 0 ~ 3개 긋는 경우의 수를 순차적으로 탐색
for max_line_cnt in range(4):
    dfs(0, max_line_cnt)

    # 가로선의 최솟값을 구해야하므로, 정답이 나왔다면 가로선을 더 긋는 경우는 탐색할 필요 없음
    if answer < 4:
        break

print(-1 if answer == 4 else answer)