arr = [1, 4, 3, 2, 7, 3]

def qsort(arr, left, right):
    pl = left
    pr = right
    x = arr[(left + right) // 2]
    
    while pl <= pr:
        while arr[pl] < x : pl += 1
        while arr[pr] > x : pr -= 1
        
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr : qsort(arr, left, pr)
    if right > pr : qsort(arr, pl, right)
    
def pythonic_qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = median_of_three(arr, 0, (len(arr)-1)//2, len(arr)-1)
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    return pythonic_qsort(left) + middle + pythonic_qsort(right)

# 배열의 첫, 마지막, 중간 번째 값들의 중간값을 피벗으로 사용
def median_of_three(arr, left, mid, right):
    values = [arr[left], arr[mid], arr[right]]
    values.sort()
    return arr.index(values[1])

arr = pythonic_qsort([2,33,4,6,2,4])
print(arr)

