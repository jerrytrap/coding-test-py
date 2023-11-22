from collections import deque


def solution(rc, operations):
    answer = [[] for _ in range(len(rc))]

    # 왼쪽 열, 오른쪽 열, 나머지 행들을 분리해서 덱으로 관리
    left_col = deque([r[0] for r in rc])
    right_col = deque([r[-1] for r in rc])
    rows = deque([deque(r[1:-1]) for r in rc])

    def rotate():
        rows[0].appendleft(left_col.popleft())
        right_col.appendleft(rows[0].pop())
        rows[-1].append(right_col.pop())
        left_col.append(rows[-1].popleft())

    def shift_row():
        rows.appendleft(rows.pop())
        left_col.appendleft(left_col.pop())
        right_col.appendleft(right_col.pop())

    for operation in operations:
        if operation == "Rotate":
            rotate()
        else:
            shift_row()

    # 행렬 다시 만들어주기
    for i in range(len(rc)):
        answer[i].append(left_col.popleft())
        answer[i] += list(rows[i])
        answer[i].append(right_col.popleft())

    return answer