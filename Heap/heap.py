
class Heap:
    
    def __init__(self):
        self.heap = []
        self.sorted = []
        

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def delete(self):
        # 힙이 비어있는 경우 처리 필요
        if len(self.heap) > 0:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            # 아직 힙이 비어있지 않다면
            if len(self.heap) > 0:
                self.heapify_down(0)
        else:
            print("힙이 비어있습니다.")
    
    def sort(self):
        while len(self.heap) > 0:
            self.sorted = [self.heap[0]] + self.sorted
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            if len(self.heap) > 0:
                
                self.heapify_down(0)
        
        print("정렬된 리스트 : ", self.sorted)
        
    def heapify_up(self, i):
        # 루트 노드일 때는 실행 X
        if i > 0:
            if self.heap[i] > self.heap[(i - 1) // 2]:
                self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
                self.heapify_up((i - 1) // 2)
    
    def heapify_down(self, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        n = len(self.heap)
        
        '''
        종료 조건
        1. 두 자식 노드 모두 존재하지 않을 때
        2. 교환이 이루어지지 않을 때
        '''

        if l < n and self.heap[l] > self.heap[largest]:
            largest = l
        if r < n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)