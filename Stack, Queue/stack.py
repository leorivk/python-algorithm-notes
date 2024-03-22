

class FixedStack:
    
    class Empty(Exception):
        '''비어 있는 FixedStack에 Pop, Peak할 때 내보내는 예외 처리'''
        pass
    
    class Full(Exception):
        '''가득 찬 FixedStack에 Push할 때 내보내는 예외 처리'''
        pass
    
    def __init__(self, capacity):
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity # 스택의 크기
        self.ptr = 0 # 스택 포인터
        
    def __len__(self):
        '''스택에 쌓여 있는 데이터 개수 반환'''
        return self.ptr
    
    def is_empty(self):
        '''스택이 비어 있는지 판단'''
        return self.ptr <= 0
    
    def is_full(self):
        '''스택이 가득 차 있는지 판단'''
        return self.ptr >= self.capacity
    
    def push(self, value):
        if self.is_full():
            return FixedStack.Full
        
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self):
        if self.is_empty():
            return FixedStack.Empty
        
        self.ptr -= 1
        return self.stk[self.ptr] # pop된 요소 반환
    
    def peak(self):
        '''꼭대기 데이터를 들여다 봄'''
        if self.is_empty():
            return FixedStack.Empty
        
        return self.stk[self.ptr - 1]
    
    def clear(self):
        self.ptr = 0
        
    def find(self, value):
        # 꼭대기 ~ 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value):
        '''스택에 있는 value의 개수를 반환'''
        cnt = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                cnt += 1
        return cnt
    
    def __contains__(self, value):
        '''스택에 value가 있는지 판단'''
        return self.count(value) > 0
    
    def dump(self):
        '''스택 안의 모든 데이터를 바닥부터 꼭대기까지 출력'''
        if self.is_empty():
            print("스택이 비어있습니다.")
        else:
            # 0 ~ self.ptr - 1
            print(self.stk[:self.ptr])