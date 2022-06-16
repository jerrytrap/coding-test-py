# Binary Search Tree
class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


root = TreeNode()
root.data = 'data'


# 노드 삽입
def insertNode(insertData):
    global root
    node = TreeNode()
    node.data = insertData

    if root == None:
        root = node

    current = root
    while True:
        if insertData < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right


# 노드 검색
def findNode(findData):
    global root
    current = root

    while True:
        if findData == current.data:
            print(findData, '있음')
            break
        elif findData < current.data:
            if current.left == None:
                print(findData, '없음')
                break
            current = current.left
        else:
            if current.right == None:
                print(findData, '없음')
                break
            current = current.right


# 노드 삭제
def deleteNode(deleteData):
    global root
    current = root
    parent = None

    while True:
        if deleteData == current.data:
            # 자식이 없는 노드일 경우, 부모 노드의 링크에 None 대입 후 삭제
            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                del current

            # 왼쪽 자식 노드가 있는 경우, 부모 노드의 링크에 자식 노드 대입
            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del current

            # 오른쪽 자식 노드가 있는 경우, 부모 노드의 링크에 자식 노드 대입
            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del current

            print(deleteData, '삭제')
            break

        elif deleteData < current.data:
            if current.left == None:
                print(deleteData, '없읎')
                break
            parent = current
            current = current.left

        else:
            if current.right == None:
                print(deleteData, '없음')
                break
            parent = current
            current = current.right


# 전위 순회
def preorder(node):
    if node == None:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


# 중위 순회
def inorder(node):
    if node == None:
        return
    preorder(node.left)
    print(node.data)
    preorder(node.right)


# 후위 순회
def postorder(node):
    if node == None:
        return
    preorder(node.left)
    preorder(node.right)
    print(node.data)

