'''
검색 대상이 오름차순으로 정렬되어 있어야 이진 탐색 가능

이진 검색의 종료 조건
1. arr[center]가 target와 일치하는 경우
2. 검색 범위가 더 이상 없는 경우
'''

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while True:
        center = (left + right) // 2
    
        if arr[center] == target:
            return center
        elif arr[center] < target:
            left = center + 1
        else:
            right = center - 1
            
        if left > right:
            break
    # 루프가 break될 때까지 탐색에 성공해서 center를 리턴하지 못했을 때 : 검색 실패
    return -1

def recursive_binary_search(arr, target, left, right):
    if left < right:
        return -1
    
    center = (left + right) // 2
    
    if arr[center] == target:
        return center
    elif arr[center] < target:
        return recursive_binary_search(arr, target, center+1, right)
    else:
        return recursive_binary_search(arr, target, left, center-1)
    


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while True:
        center = (left + right) // 2
        if target == arr[center]:
            return center
        elif target > arr[center]:
            left = center + 1
        else:
            right = center - 1
            
        if left > right:
            break
        
    return -1
