from collections import defaultdict

def solution(gems):
    answer = []
    dic = defaultdict(int)
    left_ptr = 0
    right_ptr = 0
    gem_types_size = len(set(gems))
    gems_size = len(gems)

    while left_ptr < gems_size and right_ptr < gems_size:
        dic[gems[right_ptr]] += 1
        right_ptr += 1

        #모든 종류의 보석을 포함하는 경우, 왼쪽 포인터를 한 칸씩 이동
        while len(dic) == gem_types_size:
            answer.append([left_ptr + 1, right_ptr])
            dic[gems[left_ptr]] -= 1

            if dic[gems[left_ptr]] == 0:
                del dic[gems[left_ptr]]

            left_ptr += 1

    #가장 짧은 길이이면서 가장 작은 시작 진열대 번호 구하기
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]