data = [1, 4, 3, 2, 7, 3]

def quick_sort(data, start, end):
    if start >= end:
        return data
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and data[left] <= data[pivot]:
            left += 1
        while right >= start and data[right] >= data[pivot]:
            right -= 1
        if left >= right:
            data[pivot], data[right] = data[right], data[pivot]
        else:
            data[left], data[right] = data[right], data[left]
    
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)

def pythonic_quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)



        