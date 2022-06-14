# Circular Queue
SIZE = 10
queue = [None for _ in range(SIZE)]
front = 0
rear = 0


# 큐가 꽉 찼는지 확인
def isQueueFull():
    global SIZE, queue, front, rear

    if (rear + 1) % SIZE == front:
        return True
    else:
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

    rear = (rear + 1) % SIZE
    queue[rear] = data


# 데이터 추출
def deQueue():
    global SIZE, queue, front, rear

    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None

    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


# 데이터 확인
def peek():
    global SIZE, queue, front, rear

    if isQueueEmpty():
        print("큐가 비었습니다.")
        return None

    return queue[(front + 1) % SIZE]

