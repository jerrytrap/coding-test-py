import math

def solution(m, n, startX, startY, balls):
    answer = []
    start = (startX, startY)

    for ball in balls:
        top = top_hit_dis(n, start, ball)
        bottom = bottom_hit_dis(start, ball)
        left = left_hit_dis(start, ball)
        right = right_hit_dis(m, start, ball)

        answer.append(min(top, bottom, left, right))

    return answer

def top_hit_dis(max_y, start, ball):
    if start[0] == ball[0] and start[1] < ball[1]:
        return math.inf

    return pow(max_y - start[1] + max_y - ball[1], 2) + pow(start[0] - ball[0], 2)

def bottom_hit_dis(start, ball):
    if start[0] == ball[0] and start[1] > ball[1]:
        return math.inf

    return pow(start[1] + ball[1], 2) + pow(start[0] - ball[0], 2)

def left_hit_dis(start, ball):
    if start[1] == ball[1] and start[0] > ball[0]:
        return math.inf

    return pow(start[0] + ball[0], 2) + pow(start[1] - ball[1], 2)

def right_hit_dis(max_x, start, ball):
    if start[1] == ball[1] and start[0] < ball[0]:
        return math.inf

    return pow(max_x - start[0] + max_x - ball[0], 2) + pow(start[1] - ball[1], 2)
