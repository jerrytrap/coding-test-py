# Queue
SIZE = 10
queue = [None for _ in range(SIZE)]
front = -1
rear = -1


# 큐가 꽉 찼는지 확인
def isQueueFull():
    global SIZE, queue, front, rear

    if rear != SIZE - 1:
        return False
    elif rear == SIZE - 1 and front == -1:
        return True
    else:
        for i in range(front + 1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False


# 큐가 비었는지 확인
def isQueueEmpty():
    global SIZE, queue, front, rear

    if front == rear:
        return True
    else:
        return False


# 데이터 삽입
def enQueue(data):
    global SIZE, queue, front, rear

    if isQueueFull():
        print("큐가 꽉 찼습니다.")
        return

    rear += 1
    queue[rear] = data


# 데이터 추출
def deQueue():
    global SIZE, queue, front, rear

    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None

    front += 1
    data = queue[front]
    queue[front] = None
    return data


# 데이터 확인
def peek():
    global SIZE, queue, front, rear

    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None

    return queue[front + 1]

