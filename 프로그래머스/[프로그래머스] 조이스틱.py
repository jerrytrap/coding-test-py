def solution(name):
    answer = 0
    n = len(name)

    # 알파벳 변경 (위 또는 아래 중 더 적게 조작하는 방법 선택)
    for char in name:
        answer += min(ord('Z') - ord(char) + 1, ord(char) - ord('A'))

    # 좌우로 커서 이동
    min_move = n
    for i in range(n):
        next_idx = i + 1

        # 오른쪽에서 시작해서 최종적으로 가야하는 커서의 위치는
        # 현재 커서 위치 i에서부터 A가 아닌 알파벳이 나오는 첫 지점
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        min_move = min(min_move, i * 2 + (n - next_idx), i + (n - next_idx) * 2)

    answer += min_move
    return answer
