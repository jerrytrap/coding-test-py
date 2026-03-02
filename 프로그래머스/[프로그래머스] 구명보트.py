def solution(people, limit):
    together = 0  # 무거운 사람과 같이 탈 가벼운 사람의 수
    n = len(people)
    light = 0
    heavy = n - 1

    people.sort()

    while light < heavy:
        # 현재 가장 가벼운 사람이 가장 무거운 사람과 같이 탈 수 있는 경우
        # 보트에 무거운 사람과 가벼운 사람 2명이서 타기
        if people[light] + people[heavy] <= limit:
            light += 1
            together += 1

        heavy -= 1

    # 같이 타는 가벼운 사람을 제외한 나머지는 한 보트당 한 명씩 탑승
    return n - together
