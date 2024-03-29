class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    
    def __init__(self):
        self.root = None  # 루트
        
    def search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
    
    def add(self, key, value):
        def add_node(node, key, value):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root == None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
    
    def remove(self, key):
        p = self.root  # 스캔 중인 노드
        parent = None  # 스캔 중인 노드의 부모 노드
        is_left_child = True  # p는 parent의 왼쪽 자식 노드인지 확인