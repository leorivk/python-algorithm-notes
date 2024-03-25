import hashlib

class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next
    
class ChainedHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
    
    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        
    def add(self, key):
        value = self.hash_value(key)
        current = self.table[value]
        
        while current is not None:
            if current.key == key:
                return False
            current = current.next
        
        temp = Node(key, value, self.table[value])
        self.table[value] = temp
        return True
    
    def search(self, key):
        value = self.hash_value(key)
        current = self.table[value]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def remove(self, key):
        value = self.hash_value(key)
        current = self.table[value]
        before = None
        
        while current is not None:
            if current.key == key:
                if before is None:
                    self.table[value] = current.next
                else:
                    before.next = current.next
                return True
            before = current
            current = current.next
        return False
            