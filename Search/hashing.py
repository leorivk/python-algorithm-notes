import hashlib

class Node:
    
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next
 
class ChainedHash:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key):
        
        if isinstance(key, int):
            return key % self.capacity
        
        # key 값이 int 형이 아닌 경우
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        
        # 현재 가장 상위의 노드를 다음 노드로 지정
        temp = Node(key, value, self.table[hash])
        # 가장 상위 노드로 추가
        self.table[hash] = temp
        return True
    
    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next 
        return False
    