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
        

def recursive_heapify(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if len(arr) > l: # 왼쪽 자식 노드가 있다면
        print(f"[실행] i {i} -> l {l}")
        recursive_heapify(arr, l) # 왼쪽 끝까지 내려감
        print(f"[종료] i {i} -> l {l}")
    if len(arr) > r:
        print(f"[실행] i {i} -> r {r}")
        recursive_heapify(arr, r) # 오른쪽 자식 노드가 있다면
        print(f"[종료] i {i} -> r {r}")
    
    '''
    왼쪽 자식 노드의 인덱스 : 홀수
    오른쪽 자식 노드의 인덱스 : 짝수
    '''
    parent_idx = int((i-1) // 2) if int((i-1) // 2) > 0 else 0
    
    if arr[parent_idx] < arr[i]: # 부모와 자기 자신 비교
        print(f"INDEX {i} : {arr[i]}, INDEX {parent_idx} : {arr[parent_idx]} 스왑")
        arr[i] , arr[parent_idx] = arr[parent_idx] , arr[i] # 자기 자신이 더 크면 스왑

    
arr = [2, 3, 4, 5, 7, 6]

recursive_heapify(arr, 0)

print(arr)
