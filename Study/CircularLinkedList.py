# Circular Linked List
class Node:
    def __init__(self):
        self.data = None
        self.link = None


head, current, pre = None, None, None


# 노드 삽입 함수
def insertNode(findData, insertData):
    global head, current, pre

    # 맨 앞에 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    # 중간에 노드 삽입
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 맨 뒤에 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node
    node.link = head


# 노드 삭제 함수
def deleteNode(deleteData):
    global head, current, pre

    # 첫 번째 노드 삭제
    if head.data == deleteData:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    # 첫 번째 이외 노드 삭제
    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return


# 노드 검색 함수
def findNode(findData):
    global head, current, pre

    current = head
    if current.data == findData:
        return current

    while current.link != head:
        current = current.link
        if current.data == findData:
            return current

    return Node()

