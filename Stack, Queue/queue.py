class FixedQueue:
    '''링 버퍼로 구현한 고정 길이 큐'''
    
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, capacity):
        self.no = 0 # 현재 데이터 개수
        self.front = 0 
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
        
    def __len__(self):
        return self.no
    
    def is_empty(self):
        return self.no <= 9
    
    def is_full(self):
        return self.no >= self.capacity
    
    def enque(self, x):
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            '''rear값이 큐의 크기인 capacity와 같을 경우 rear를 배열의 맨 앞 인덱스로 되돌림 (링 버퍼)'''
            self.rear = 0
        
    def deque(self):
        if self.is_empty():
            raise FixedQueue.Empty
        
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            '''front값이 큐의 크기인 capacity와 같을 경우 front를 배열의 맨 앞 인덱스로 되돌림 (링 버퍼)'''
            self.front = 0
        
        return x

    def peek(self):
        '''맨 앞 데이터를 들여다 봄'''
        if self.is_empty():
            raise FixedQueue.Empty
        
        return self.queue[self.front]
    
    def find(self, value):
        for i in range(self.no):
            idx = (i + self.front) % self.capacity # 큐 선형 검색
            if self.que[idx] == value:
                return idx
            
    def count(self, value):
        cnt = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                cnt += 1
        return cnt

    def __contains__(self, value):
        return self.count(value)
    
    def clear(self):
        self.no = self.front = self.rear = 0
        
    def dump(self):
        if self.is_empty():
            print("큐가 비었습니다.")
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end='')
            print()