# Stack
SIZE = 10
stack = [None for _ in range(SIZE)]
top = -1


# 스택이 꽉 찼는지 확인
def isStackFull():
    global SIZE, stack, top

    if top >= SIZE - 1:
        return True
    else:
        return False


# 스택이 비었는지 확인
def isStackEmpty():
    global SIZE, stack, top

    if top == -1:
        return True
    else:
        return False


# 데이터 삽입
def push(data):
    global SIZE, stack, top

    if isStackFull():
        print("스택이 꽉 찼습니다.")
        return

    top += 1
    stack[top] = data


# 데이터 추출
def pop():
    global SIZE, stack, top

    if isStackEmpty():
        print("스택이 비었습니다.")
        return None

    data = stack[top]
    stack[top] = None
    top -= 1
    return data


# 데이터 확인
def peek():
    global SIZE, stack, top

    if isStackEmpty():
        print("스택이 비었습니다.")
        return None

    return stack[top]

