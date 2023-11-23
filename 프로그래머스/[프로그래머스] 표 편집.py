class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

def make_linked_list(head, n):
    prev_node = head

    for i in range(1, n):
        new_node = Node(i)
        prev_node.next = new_node
        new_node.prev = prev_node
        prev_node = new_node

    return head

def move_cursor(cur, k, dir):
    if dir == 'UP':
        for _ in range(k):
            cur = cur.prev
    else:
        for _ in range(k):
            cur = cur.next

    return cur

def remove_node(node):
    prev_node = node.prev
    next_node = node.next

    if prev_node is not None:
        prev_node.next = next_node

    #마지막 노드라면 이전 노드를, 그렇지 않다면 다음 노드를 선택
    if next_node is not None:
        next_node.prev = prev_node
        return next_node
    else:
        return prev_node

def restore_node(node):
    prev_node = node.prev
    next_node = node.next

    if prev_node is not None:
        prev_node.next = node
    if next_node is not None:
        next_node.prev = node

def solution(n, k, cmd):
    head = make_linked_list(Node(0), n)
    cursor = move_cursor(head, k, 'DOWN')
    removed_nodes = []
    ans = ['O' for _ in range(n)]

    for c in cmd:
        if c[0] == 'U':
            command, value = c.split()
            cursor = move_cursor(cursor, int(value), 'UP')
        elif c[0] == 'D':
            command, value = c.split()
            cursor = move_cursor(cursor, int(value), 'DOWN')
        elif c[0] == 'C':
            removed_nodes.append(cursor)
            cursor = remove_node(cursor)
        else:
            node = removed_nodes.pop()
            restore_node(node)

    for node in removed_nodes:
        ans[node.data] = 'X'

    return ''.join(ans)
