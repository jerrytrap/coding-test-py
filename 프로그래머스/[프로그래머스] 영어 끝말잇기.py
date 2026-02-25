def solution(n, words):
    prev = words[0]
    used_words = set([prev])

    for i in range(1, len(words)):
        cur = words[i]
        user = (i % n) + 1
        turn = (i // n) + 1

        # 앞 단어의 마지막 문자로 시작되는 단어가 아니거나
        # 이미 사용된 단어인 경우
        if prev[-1] != cur[0] or cur in used_words:
            return [user, turn]

        used_words.add(cur)
        prev = cur

    return [0, 0]
