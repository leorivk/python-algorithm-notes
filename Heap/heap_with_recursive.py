def recursive_heapify(arr, i):

    l = 2 * i + 1
    r = 2 * i + 2
    if len(arr) > l:
        recursive_heapify(arr, l)
    if len(arr) > r:
        recursive_heapify(arr, r) 
    
    parent = int((i-1) // 2) if int((i-1) // 2) > 0 else 0

    if arr[parent] < arr[i]: 
        arr[i] , arr[parent] = arr[parent] , arr[i]
        recursive_heapify(arr, i)

def test_recursive_heapify(arr, i):

    l = 2 * i + 1
    r = 2 * i + 2
    if len(arr) > l: # 왼쪽 자식 노드가 있다면
        print(f"[실행] i {i} -> l {l}")
        test_recursive_heapify(arr, l) # 왼쪽 끝까지 내려감
        print(f"[종료] i {i} -> l {l}")
    if len(arr) > r:
        print(f"[실행] i {i} -> r {r}")
        test_recursive_heapify(arr, r) # 오른쪽 자식 노드가 있다면
    
    parent = int((i-1) // 2) if int((i-1) // 2) > 0 else 0

    if arr[parent] < arr[i]: # 부모와 자기 자신 비교
        print(f"INDEX {i} : {arr[i]}, INDEX {parent} : {arr[parent]} 스왑")
        arr[i] , arr[parent] = arr[parent] , arr[i] # 자기 자신이 더 크면 스왑
        test_recursive_heapify(arr, i)

arr = [3,4,6,1,9,2,8,7]

test_recursive_heapify(arr, 0)

print(f"Heapify array: {arr}")

