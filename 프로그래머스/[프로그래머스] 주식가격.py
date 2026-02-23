def solution(prices):
    stack = [] # 주식 가격이 기록된 "시각" 저장
    total_time = len(prices)
    answer = [0 for _ in range(total_time)]

    for current_time in range(total_time):
        # 현재 가격이 과거 가격보다 감소했다면, 가격이 떨어지지 않은 기간을 계산해서 기록하고 스택에서 제거
        while stack and prices[stack[-1]] > prices[current_time]:
            past_time = stack.pop()
            answer[past_time] = current_time - past_time

        stack.append(current_time)

    # 스택에 남아있는 주식은 끝까지 가격이 떨어지지 않음
    while stack:
        past_time = stack.pop()
        answer[past_time] = total_time - past_time - 1

    return answer
