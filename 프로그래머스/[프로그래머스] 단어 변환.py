from collections import deque

def compare(str1, str2):
    cnt = 0

    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            cnt += 1

        if cnt > 1:
            return False

    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = {begin}

    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            return cnt

        # 한 글자만 바꿔서 만들 수 있는 단어라면 큐에 추가
        for word in words:
            if word not in visited and compare(cur, word):
                visited.add(word)
                queue.append((word, cnt + 1))

    return 0
