def make_same_sum(queue1, queue2, target):
    answer = []
    array = queue1 + queue2 #두 큐를 합쳐서 배열처럼 두고 계산
    queue_length = len(queue1)
    move = 0
    max_move = queue_length * 4 #큐 한 개의 길이 * 4 (투포인터 최대 이동 횟수)
    left_ptr = 0
    right_ptr = 0
    one_queue_sum = 0 #한 쪽 큐의 합

    while move < max_move:
        if right_ptr >= len(array) or left_ptr >= len(array):
            break

        if one_queue_sum == target:
            #(right-left)만큼 오른쪽 큐로, 오른쪽 큐는 전부 왼쪽으로 이동
            if right_ptr < queue_length:
                answer.append(right_ptr - left_ptr + queue_length)
            #(right-length)만큼 왼쪽 큐로, left만큼 오른쪽 큐로 이동
            else:
                answer.append(right_ptr - queue_length + left_ptr)

            one_queue_sum += array[right_ptr]
            right_ptr += 1
        elif one_queue_sum <= target:
            one_queue_sum += array[right_ptr]
            right_ptr += 1
        else:
            one_queue_sum -= array[left_ptr]
            left_ptr += 1

        move += 1

    return answer

def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    target = total_sum // 2

    #두 큐의 총 합이 홀수이면, 답을 구할 수 없음
    if total_sum % 2 != 0:
        return -1

    #두 큐의 원소의 합을 같게 만들기
    answer = make_same_sum(queue1, queue2, target)

    if len(answer) == 0:
        return -1
    else:
        return min(answer)