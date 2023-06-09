def solution(s):
    answer = len(s)

    # s를 1부터 s 길이의 절반까지 잘라서 확인
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        substr = "" # 확인할 문자열
        cnt = 1

        # 확인할 문자열 다음부터 같은 길이만큼 잘라가며 비교
        for j in range(0, len(s) + 1, i):
            compare = s[j:j + i]
            # 같을 경우 카운트 증가
            if substr == compare:
                cnt += 1

            # 다를 경우 확인할 문자열과 카운트를 더함 (카운트가 2 이상일 때만)
            else:
                compressed += str(cnt) + compare if cnt >= 2 else compare

                # 다음 문자열을 비교
                substr = compare
                cnt = 1

        answer = min(answer, len(compressed))
    return answer
