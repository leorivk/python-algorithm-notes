def heapify(arr, n, i):
    largest = i # 초기 가장 큰 요소를 i로 설정 (루트)
    l = 2 * i + 1 # 왼쪽 자식 노드
    r = 2 * i + 2 # 오른쪽 자식 노드
    
    # 왼쪽 자식이 존재하고, 현재 가장 큰 값보다 큰 경우
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    # 오른쪽 자식이 존재하고, 현재 가장 큰 값보다 큰 경우
    if r < n and arr[r] > arr[largest]:
        largest = r
        
    # 가장 큰 값이 루트가 아닌 경우
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # 스왑
        
        heapify(arr, n, largest)
    
def heap_sort(arr):
    n = len(arr)
    
    # arr[i] ~ arr[n-1]을 힙으로 만들기
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # 최댓값인 a[0]와 마지막 원소 교환
        heapify(arr, i, 0) # arr[0] ~ arr[i]을 힙으로 만들기 (힙 사이즈 줄이고 힙 속성 유지)
