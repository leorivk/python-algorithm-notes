data = [5, 7, 9, 0, 3, 1, 2, 3, 8]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(data))