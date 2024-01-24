def add_zero(num):
    node_count = len(num)
    bin_node_count = bin(node_count)[2:]
    zero_count = 0

    if '0' in bin_node_count:
        zero_count = (1 << len(bin_node_count)) - 1 - node_count
    return '0' * zero_count + num

def check_binary_tree(bin_num, mid, offset):
    if offset == 0:
        return True
    elif bin_num[mid] == '0':
        if bin_num[mid - offset] == '1' or bin_num[mid + offset] == '1':
            return False

    return check_binary_tree(bin_num, mid - offset, offset // 2) and check_binary_tree(bin_num, mid + offset, offset // 2)

def solution(numbers):
    answer = [0 for _ in range(len(numbers))]

    for i, num in enumerate(numbers):
        if num == 0:
            continue
        bin_num = add_zero(bin(num)[2:])
        node_count = len(bin_num)
        offset = (node_count + 1) // 4

        if(check_binary_tree(bin_num, node_count // 2, offset)):
            answer[i] = 1
    return answer
