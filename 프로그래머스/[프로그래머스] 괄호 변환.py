def get_u_and_v(w):
    for i in range(0, len(w) - 2, 2):
        u = w[:i + 2]

        if is_balanced(u):
            return u, w[i + 2:]

    return w, ""

def is_balanced(string):
    count = 0

    for s in string:
        if s == "(":
            count += 1
        else:
            count -= 1

    return count == 0

def is_correct(string):
    stack = []

    for s in string:
        if not stack:
            stack.append(s)
            continue

        if (stack[-1] == "(" and s == ")") or (stack[-1] == "(" and s == ")"):
            stack.pop()
        else:
            stack.append(s)

    return len(stack) == 0

def reverse(string):
    temp = ""

    for s in string:
        if s == "(":
            temp += ")"
        else:
            temp += "("

    return temp

# 올바른 문자로 변환
def transform(w):
    # [1] 빈 문자열 반환
    if w == "":
        return ""

    # [2] u, v 구하기
    u, v = get_u_and_v(w)

    # [3] u가 올바른 경우
    if is_correct(u):
        # [3-1]
        return u + transform(v)
    # [4] u가 올바르지 않은 경우
    else:
        # [4-1] ~ [4-5]
        return "(" + transform(v) + ")" + reverse(u[1:-1])

def solution(p):
    return transform(p)
