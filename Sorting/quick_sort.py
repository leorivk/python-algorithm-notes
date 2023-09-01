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


quick_sort(data, 0, len(data)-1)
print(data)

        