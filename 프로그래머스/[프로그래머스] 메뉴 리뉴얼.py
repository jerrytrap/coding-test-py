from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    for c in course:
        combs = []
        menu = defaultdict(int)

        # 주문 받은 메뉴 구성 중 c개를 선택해서 만들 수 있는 조합을 모두 구함
        for order in orders:
            combs.extend(list(combinations(sorted(order), c)))

        # 만들 수 있는 조합이 없으면 넘어감
        if not combs:
            continue

        for comb in combs:
            menu[''.join(comb)] += 1

        max_order_count = max(menu.values())
        for menu_name, ordered_count in menu.items():
            # 가장 많이 주문된 메뉴 조합이고, 2번 이상 주문 된 경우
            if ordered_count == max_order_count and ordered_count >= 2:
                answer.append(menu_name)

    return sorted(answer)
