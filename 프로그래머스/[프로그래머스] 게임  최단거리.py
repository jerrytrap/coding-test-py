from collections import deque


def compare(str1, str2):
    cnt = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt
        for w in words:
            if compare(word, w):
                queue.append([w, cnt + 1])

    return 0
