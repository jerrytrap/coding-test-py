from collections import Counter

def solution(want, number, discount):
    answer = 0
    item_count = 10
    info = {w: n for w, n in zip(want, number)} # 원하는 제품과 수량

    # 1 ~ 10일차부터 시작
    current_dict = Counter(discount[:10])
    if info == current_dict:
        answer += 1

    # i일차를 제거하고 i + 10일차를 추가하면서 비교
    for i in range(len(discount) - item_count):
        # i일차 제거
        out_item = discount[i]
        current_dict[out_item] -= 1

        # 비교를 위해 개수가 0인 경우는 제거해주기
        if current_dict[out_item] == 0:
            del current_dict[out_item]

        # i + 10일차 추가
        in_item = discount[i + item_count]
        current_dict[in_item] += 1

        # 원하는 제품과 수량이 일치하는 경우
        if info == current_dict:
            answer += 1

    return answer
